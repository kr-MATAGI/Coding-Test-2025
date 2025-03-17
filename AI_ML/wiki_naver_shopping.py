import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

# Load Data
train_df = pd.read_csv("./naver_shopping/naver_shopping_train.csv")
test_df = pd.read_csv("./naver_shopping/naver_shopping_test.csv")
'''
   ID       판매가  화면크기  형태   해상도  화면비율  LCD  LED  OLED  QLED  단자  부가기능
0   8  396240.0    55   0  2160     1    0    1     0     0   3     1
1   9  412870.0    55   0  2160     1    0    1     0     0   3     1
2  10  414590.0    55   0  2160     1    0    1     0     0   3     1
3  14  418000.0    55   0  2160     1    0    1     0     0   3     1
4  15  419000.0    55   0  2160     1    0    1     0     0   3     1
'''


# Split Data
x_train = train_df.drop(["판매가", "ID"], axis=1)
y_train = train_df["판매가"]

x_test = test_df.drop(["판매가", "ID"], axis=1)
y_test = test_df["판매가"]

print(x_train.shape)

# Check NaN
# print(x_train.isnull().sum())
# print(x_test.isnull().sum())

# Model
model = RandomForestRegressor()
model.fit(x_train, y_train)

# Valid
print(model.score(x_test, y_test))

# Predict
new_pred = np.array([
    [55, 0, 2160, 1, 0, 1, 0, 0, 3, 1]
])
print(new_pred.shape)

print(model.predict(new_pred))