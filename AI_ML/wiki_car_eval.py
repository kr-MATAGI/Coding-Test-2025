import pandas as pd
import xgboost as xgb

from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.model_selection import train_test_split

# Load Data
total_data = pd.read_csv("./car_eval/car_eval.csv")
print(f"total_data.size: {total_data.shape[0]}")

x_data = total_data.drop(["class values"], axis=1)
y_data = total_data["class values"]
print(x_data.head())
print(y_data)

# Convert - doors,persons (more)
max_doors = list(set(x_data["doors"].values))
x_data["doors"] = x_data["doors"].str.replace("5more", "6")
x_data["doors"] = x_data["doors"].astype(int)

max_persons = list(set(x_data["persons"].values))
x_data["persons"] = x_data["persons"].str.replace("more", "5")
x_data["persons"] = x_data["persons"].astype(int)

# print(x_data.head())

# OneHot
col_trans = make_column_transformer(
    (OneHotEncoder(), ["buyingprice","maint","lug_boot","safety", "doors", "persons"]),
    remainder="passthrough"
)
col_trans.fit(x_data)
print(x_data.head())
x_data = col_trans.transform(x_data)
# print(x_data.head())

# Label Encode
label_enc = LabelEncoder()
label_enc.fit(y_data)
y_data = label_enc.transform(y_data)

# Split Train / Test
train_x, test_x, train_y, test_y = train_test_split(
    x_data, y_data, test_size=0.2, random_state=42, stratify=y_data
)
print(f"Train Size - x: {train_x.shape}, y: {train_y.shape}")
print(f"Test Size - x: {test_x.shape}, y: {test_y.shape}")

# Model
model = xgb.XGBClassifier(
    random_state=42
)
model.fit(train_x, train_y)

# Valid
print(model.score(train_x, train_y))

# Test
print(model.score(test_x, test_y))

x_test = [
    ['vhigh', 'vhigh', 2, 2, 'small', 'low']
]
x_test = pd.DataFrame(x_test, columns=['buyingprice', 'maint', 'doors', 'persons', 'lug_boot', 'safety'])
x_test = col_trans.transform(x_test)
y_predict = model.predict(x_test)
y_prob = model.predict_proba(x_test)
print(label_enc.inverse_transform(y_predict), y_prob)
