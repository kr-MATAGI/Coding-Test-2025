import pandas as pd
import xgboost as xgb
import numpy as np

from sklearn.metrics import mean_squared_log_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer

"""
['id', 'vendor_id', 'pickup_datetime', 'dropoff_datetime',
'passenger_count', 'pickup_longitude', 'pickup_latitude',
'dropoff_longitude', 'dropoff_latitude', 'store_and_fwd_flag',
'trip_duration']

    id  vendor_id   pickup_datetime  ... dropoff_latitude  store_and_fwd_flag  trip_duration
0  id2560881          1  2016-01-18 11:10  ...        40.762867                   N              4
1  id3059620          1  2016-01-06 21:53  ...        40.726780                   N             35
2  id2310998          2  2016-02-21 23:01  ...        40.644859                   N             33
3  id3472462          1   2016-02-08 0:05  ...        40.759983                   N             32
4  id1271427          1  2016-06-26 13:52  ...        40.781155                   N             20
"""

# Load Data
train_data = pd.read_csv("./taxi/train.csv")
test_data = pd.read_csv("./taxi/test.csv")
print(f"""
Data Size: train-{train_data.shape}, test-{test_data.shape}
{train_data.columns}
{train_data.head()}
""")

train_data = train_data.drop(["id"], axis=1)
test_data = test_data.drop(["id"], axis=1)


# Convert X,y
train_data['pickup_datetime'] = pd.to_datetime(train_data['pickup_datetime'])
test_data['pickup_datetime'] = pd.to_datetime(test_data['pickup_datetime'])

train_data['dropoff_datetime'] = pd.to_datetime(train_data['dropoff_datetime'])

# pickup
train_data['pickup_year'] = train_data['pickup_datetime'].dt.year
train_data['pickup_month'] = train_data['pickup_datetime'].dt.month
train_data['pickup_day'] = train_data['pickup_datetime'].dt.day
train_data['pickup_hour'] = train_data['pickup_datetime'].dt.hour
train_data['pickup_minute'] = train_data['pickup_datetime'].dt.minute

test_data['pickup_year'] = test_data['pickup_datetime'].dt.year
test_data['pickup_month'] = test_data['pickup_datetime'].dt.month
test_data['pickup_day'] = test_data['pickup_datetime'].dt.day
test_data['pickup_hour'] = test_data['pickup_datetime'].dt.hour
test_data['pickup_minute'] = test_data['pickup_datetime'].dt.minute

# dropoff
train_data['dropoff_year'] = train_data["dropoff_datetime"].dt.year
train_data["dropoff_month"] = train_data["dropoff_datetime"].dt.month
train_data["dropoff_day"] = train_data["dropoff_datetime"].dt.day
train_data["dropoff_hour"] = train_data["dropoff_datetime"].dt.hour
train_data["dropoff_minute"] = train_data["dropoff_datetime"].dt.minute

train_data = train_data.drop(["pickup_datetime", "dropoff_datetime"], axis=1)
test_data = test_data.drop(["pickup_datetime"], axis=1)
print(f"{train_data.columns}")

# Check NaN
print(f"""
train -
{train_data.isnull().sum()}
test -
{test_data.isnull().sum()}
""")

# Split X, y
target_feature = [
    "dropoff_year", "dropoff_month", "dropoff_day",
    "dropoff_hour", "dropoff_minute",
    "trip_duration"
]
train_x = train_data.drop(target_feature, axis=1)
train_y = train_data["trip_duration"]

# OneHot Encoding
onehot_enc = make_column_transformer(
    (OneHotEncoder(sparse_output=False, handle_unknown="ignore"), ["store_and_fwd_flag"]),
    remainder="passthrough"
)
onehot_enc.fit(train_x)


train_x = onehot_enc.transform(train_x)
test_data = onehot_enc.transform(test_data)

# train_x = pd.DataFrame(train_x, columns=onehot_enc.get_feature_names_out())
# print(train_x.head())


# Model
print(f"Start Train !")
model = RandomForestRegressor()
model.fit(train_x, train_y)
print(f"END Train !")

# Score
train_pred = model.predict(train_x)
print(f"train_pred:\n{train_pred}")
train_score = np.sqrt(mean_squared_log_error(train_y, train_pred))
print(f"train_pred_score: {train_score}")


# Test Set
test_pred = model.predict(test_data)
print(f"train_pred_score: {test_pred}")

# Load Sample
sample_df = pd.read_csv("./taxi/sample-submission.csv")
sample_df['trip_duration'] = test_pred
sample_df.to_csv("./taxi/answer.csv", index=False)