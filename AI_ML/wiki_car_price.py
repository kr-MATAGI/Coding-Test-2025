import pandas as pd
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.compose import make_column_transformer
from sklearn.linear_model import Lasso, LinearRegression
from sklearn.ensemble import RandomForestRegressor

# Load Data
train_df = pd.read_csv("./car_price/carprice_train.csv")
test_df = pd.read_csv("./car_price/carprice_test.csv")

x_train = train_df.drop("가격", axis=1)
y_train = train_df["가격"]

x_test = test_df.drop("가격", axis=1)
y_test = test_df["가격"]

'''
     년식   종류    연비   마력    토크   연료  하이브리드   배기량    중량 변속기
0  2015  준중형  11.8  172  21.0  가솔린      0  1999  1300  자동
1  2015  준중형  12.3  204  27.0  가솔린      0  1591  1300  자동
2  2015   소형  15.0  100  13.6  가솔린      0  1368  1035  수동
3  2014   소형  14.0  140  17.0  가솔린      0  1591  1090  자동
4  2015   대형   9.6  175  46.0   디젤      0  2497  1990  자동
'''

# print(x_train.shape, y_train.shape)
# print(x_test.shape, y_test.shape)

# print(x_train.head())

# NaN
# print(x_train.isnull().sum())
# print(x_test.isnull().sum())

# OneHot
transformer = make_column_transformer(
    (OneHotEncoder(), ["종류", "연료", "하이브리드", "변속기"]),
    remainder="passthrough"
)
transformer.fit(x_train)
x_train = transformer.transform(x_train)
x_test = transformer.transform(x_test)

# model
model = LinearRegression()
model.fit(x_train, y_train)

# Valid
print(model.score(x_test, y_test))

temp_df = pd.DataFrame(
    [[2015,"중형",14.8,200,43,"디젤",0,2199,1760,"수동"]],
    columns=[
        '년식', '종류', '연비', '마력', '토크', 
        '연료', '하이브리드', '배기량', '중량', '변속기'
    ]
)
temp_df = transformer.transform(temp_df)
ans = model.predict(temp_df)
print(ans)