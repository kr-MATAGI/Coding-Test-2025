import pandas as pd
import numpy as np

from sklearn.metrics import mean_squared_log_error
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import RobustScaler, MinMaxScaler
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor
from sklearn.linear_model import Lasso
from sklearn.model_selection import GridSearchCV

import xgboost as xgb

'''
    datetime  season  holiday  workingday  weather  ...  humidity  windspeed  casual  registered  count
0  2012-12-07 14:00       4        0           1        2  ...        71    11.0014      40         175    215
1   2012-06-17 1:00       2        0           0        1  ...        60    11.0014      21          67     88
2  2012-07-05 22:00       3        0           1        1  ...        59     8.9981      63         162    225
3  2011-07-17 12:00       3        0           0        1  ...        55    19.0012     177         243    420
4  2011-11-09 15:00       4        0           1        1  ...        45    15.0013      21         130    151
'''


# Load data
train_df = pd.read_csv("./bycle/train.csv")
test_df = pd.read_csv("./bycle/test.csv")

# Shuffle
# train_df = train_df.sample(frac=1).reset_index(drop=True)

# Sort
train_df["datetime"] = pd.to_datetime(train_df["datetime"])
test_df["datetime"] = pd.to_datetime(test_df["datetime"])

train_df = train_df.sort_values(by="datetime", ascending=True)
# test_df = test_df.sort_values(by="datetime")
# print(train_df.head())

# Split datetime
train_df["year"] = train_df["datetime"].dt.year
train_df["month"] = train_df["datetime"].dt.month
train_df["day"] = train_df["datetime"].dt.day
train_df["hour"] = train_df["datetime"].dt.hour
train_df["weekday"] = train_df["datetime"].dt.weekday


test_df["year"] = test_df["datetime"].dt.year
test_df["month"] = test_df["datetime"].dt.month
test_df["day"] = test_df["datetime"].dt.day
test_df["hour"] = test_df["datetime"].dt.hour
test_df["weekday"] = test_df["datetime"].dt.weekday

train_df = train_df.drop(["datetime"], axis=1)
test_df = test_df.drop(["datetime"], axis=1)

# Make data
train_x = train_df.drop(["casual", "registered", "count"], axis=1)
train_y = train_df.loc[:, ["count"]]
print(f"train - x: {train_x.shape}, y: {train_y.shape}")

# test_df = test_df.drop("temp", axis=1)

# Check NaN
# print(train_x.isnull().sum())

# Scaler
# wind_scaler = RobustScaler()
# print(train_df["windspeed"].describe())

# print(train_df["windspeed"])
# train_x["windspeed"] = wind_scaler.fit_transform(train_x[["windspeed"]])
# print(train_df["windspeed"])
# print(train_df["windspeed"].describe())

# 윈드 speed가 0 인 애들 삭제
# print(f"Before Wind Speed del : {train_df.shape}")

# valid_index = train_x.loc[train_x["windspeed"] != 0].index
# train_x = train_x.loc[valid_index].reset_index(drop=True)
# train_y = train_y.loc[valid_index].reset_index(drop=True)

# print(f"After Wind Speed del : {train_df.shape}")


# humidity_scaler = RobustScaler()
# train_x["humidity"] = humidity_scaler.fit_transform(train_x[["humidity"]])

# Group
# print(train_x["temp"].describe())
# train_x["TempGroup"] = pd.qcut(train_x["temp"], q=4, labels=[0,1,2,4]).astype(int)
# test_df["TempGroup"] = pd.qcut(test_df["temp"], q=4, labels=[0,1,2,4]).astype(int)

# train_x["aTempGroup"] = pd.qcut(train_x["temp"], q=4, labels=[0,1,2,4]).astype(int)
# test_df["aTempGroup"] = pd.qcut(test_df["temp"], q=4, labels=[0,1,2,4]).astype(int)

# train_x = train_x.drop("temp", axis=1)
# test_df = test_df.drop("temp", axis=1)

# train_x = train_x.drop("atemp", axis=1)
# test_df = test_df.drop("atemp", axis=1)

# print(train_x["TempGroup"][:5])

# exit()

# Hyperparameter
# hy_params = {
#     "n_estimators": [100, 200, 300],
#     "max_depth": [3,6,9],
#     # "learning_rate": [0.01, 0.1, 0.3],
# }
# optimer = GridSearchCV(
#     RandomForestRegressor(random_state=42),
#     cv=5,
#     n_jobs=-1,
#     param_grid=hy_params,
#     scoring='accuracy',
# )
# optimer.fit(train_x, train_y)
# best_params = optimer.best_params_
# print(f"best_params: {best_params}")

# Model
model = RandomForestRegressor(
    # random_state=42,
    n_estimators=400,
    # **best_params
)
model.fit(
    train_x, train_y,
    # eval_metric=msle_eval,
)

# Valid Train
y_valid_predict = model.predict(train_x)
rmsle = np.sqrt(mean_squared_log_error(train_y, y_valid_predict))
print("Validation RMSLE: {:.4f}".format(rmsle))

# Test
test_y = model.predict(test_df)

answer_df = pd.read_csv("./bycle/sample-submission.csv")
answer_df["count"] = test_y
answer_df["count"] = answer_df["count"].astype(int)
answer_df.loc[answer_df["count"] < 0, "count"] = 0
print(answer_df)

# answer_df = answer_df.loc[:, ["datetime", "count"]]
answer_df.to_csv("./bycle/sample-submission.csv", index=False)

# import pandas as pd
# import numpy as np
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import mean_squared_log_error
# from sklearn.model_selection import train_test_split

# # 데이터 불러오기
# train_df = pd.read_csv('./bycle/train.csv')
# test_df = pd.read_csv('./bycle/test.csv')

# # datetime 변환 및 특성 추출
# def add_datetime_features(df):
#     df['datetime'] = pd.to_datetime(df['datetime'])
#     df['year'] = df['datetime'].dt.year
#     df['month'] = df['datetime'].dt.month
#     df['day'] = df['datetime'].dt.day
#     df['hour'] = df['datetime'].dt.hour
#     df['weekday'] = df['datetime'].dt.weekday
#     return df

# train_df = add_datetime_features(train_df)
# test_df = add_datetime_features(test_df)

# # 사용할 특성 선택
# features = ['season', 'holiday', 'workingday', 'weather', 'temp', 'atemp',
#             'humidity', 'windspeed', 'year', 'month', 'day', 'hour', 'weekday']

# X = train_df[features]
# y = train_df['count']

# # 모델 평가를 위한 train/validation 분리
# # X, X_val, y_train, y_val = train_test_split(X, y, test_size=0.0, random_state=42)

# # 모델 학습: RandomForestRegressor 사용
# model = RandomForestRegressor(n_estimators=100, random_state=42)
# model.fit(X, y)

# # 검증 셋에 대한 예측 및 RMSLE 계산
# y_val_pred = model.predict(X)
# rmsle = np.sqrt(mean_squared_log_error(y, y_val_pred))
# print("Validation RMSLE: {:.4f}".format(rmsle))

# # 테스트 셋 예측
# X_test = test_df[features]
# test_pred = model.predict(X_test)

# # submission 파일 생성 (data_id와 예측한 count)
# submission = pd.DataFrame({
#     'datetime': test_df['datetime'],
#     'count': test_pred
# })
# submission.to_csv('./bycle/submission.csv', index=False)
# print("Submission 파일이 생성되었습니다.")