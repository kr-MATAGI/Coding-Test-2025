import pandas as pd
import numpy as np

from xgboost import XGBRegressor
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV

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

# Hyperparameter
param_grid = {
    'n_estimators': [100, 200, 300], # 트리 개수
    'max_depth': [10, 15, 20], # 트리 최대 깊이
    'min_samples_split': [2, 5, 10] # 노드를 나누는 최소 샘플 수
}

grid_search = GridSearchCV(
    RandomForestRegressor(random_state=42), 
    param_grid=param_grid,
    cv=5,  # 5-Fold 교차 검증
    scoring='r2', # R^2 점수 기준 최적화
    n_jobs=-1 # 모든 CPU 코어 사용
)
grid_search.fit(x_train, y_train)
best_params = grid_search.best_params_
print(f"Optim Hyperparameter:\n{best_params}")

# Model
model = XGBRegressor(
    # n_estimators=best_params['n_estimators'],
    # max_depth=best_params['max_depth'],
    # min_samples_split=best_params['min_samples_split']
)
model.fit(x_train, y_train)

# Valid
print(model.score(x_test, y_test))

# Predict
new_pred = np.array([
    [55, 0, 2160, 1, 0, 1, 0, 0, 3, 1]
])
print(new_pred.shape)

print(model.predict(new_pred))