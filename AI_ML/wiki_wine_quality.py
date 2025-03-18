import pandas as pd
import xgboost as xgb

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, GridSearchCV


'''
      fixed acidity  volatile acidity  citric acid  residual sugar  ...    pH  sulphates  alcohol  quality
0               7.4             0.700         0.00             1.9  ...  3.51       0.56      9.4        5
1               7.8             0.880         0.00             2.6  ...  3.20       0.68      9.8        5
2               7.8             0.760         0.04             2.3  ...  3.26       0.65      9.8        5
3              11.2             0.280         0.56             1.9  ...  3.16       0.58      9.8        6
4               7.4             0.700         0.00             1.9  ...  3.51       0.56      9.4        5
...             ...               ...          ...             ...  ...   ...        ...      ...      ...
1594            6.2             0.600         0.08             2.0  ...  3.45       0.58     10.5        5
1595            5.9             0.550         0.10             2.2  ...  3.52       0.76     11.2        6
1596            6.3             0.510         0.13             2.3  ...  3.42       0.75     11.0        6
1597            5.9             0.645         0.12             2.0  ...  3.57       0.71     10.2        5
1598            6.0             0.310         0.47             3.6  ...  3.39       0.66     11.0        6

[1599 rows x 12 columns]
'''

# Load Data
total_df = pd.read_csv("./wine/winequality-red.csv")
total_size = total_df.shape[0]
print(f"total_size: {total_size}")

x_data = total_df.drop(["quality", "density", "chlorides"], axis=1)
y_data = total_df["quality"]

label_enc = LabelEncoder()
label_enc.fit(y_data)
y_data = label_enc.transform(y_data)

# print(y_data)

# 그룹화
print(f"residual sugar min/max: {x_data['residual sugar'].min()}/{x_data['residual sugar'].max()}")
x_data["residual sugar"] = pd.cut(x_data["residual sugar"], bins=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],labels=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
x_data["residual sugar"] = x_data["residual sugar"].astype(int)

train_x, test_x, train_y, test_y = train_test_split(
    x_data, y_data, test_size=0.3, random_state=42, stratify=y_data
)
print(f"shape - train(x: {train_x.shape[0]}, y: {train_y.shape[0]})")
print(f"shape - test(x: {test_x.shape[0]}, y: {test_y.shape[0]})")

# Hyperparameter
param_grid = {
    'n_estimators': [100, 200, 300],  # 트리 개수 축소
    'max_depth': [3, 6, 9],  # 트리 최대 깊이 축소
    'learning_rate': [0.01, 0.1, 0.3],  # 학습률 축소
    'subsample': [0.8, 1.0],  # 샘플링 비율 유지
    'colsample_bytree': [0.8, 1.0],  # 특성 샘플링 비율 유지
}

grid_model = GridSearchCV(
    xgb.XGBClassifier(
        random_state=42,
        eval_metric='mlogloss'
    ),
    param_grid=param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)
grid_model.fit(train_x, train_y)

best_params = grid_model.best_params_
print(best_params)

# Check NaN
# print(train_x.isnull().sum())
# print(test_x.isnull().sum())

# Round
# print(train_x.loc[9:13, "chlorides"])
# train_x["chlorides"] = train_x["chlorides"].round(3)
# print(train_x.loc[9:13, "chlorides"])


# Summary
print(train_x.describe())


# Model
model = xgb.XGBClassifier(
    random_state=42,
    eval_metric='mlogloss',
    **best_params
)
model.fit(train_x, train_y)

# Valid
print(model.score(train_x, train_y))

# predict
print(model.predict(test_x))

print(model.score(test_x, test_y))