import pandas as pd
import xgboost as xgb
import numpy as np

from sklearn.preprocessing import MinMaxScaler, OneHotEncoder, LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression, Lasso
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV

'''
    Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm      Species
0   1            5.1           3.5            1.4           0.2  Iris-setosa
1   2            4.9           3.0            1.4           0.2  Iris-setosa
2   3            4.7           3.2            1.3           0.2  Iris-setosa
3   4            4.6           3.1            1.5           0.2  Iris-setosa
4   5            5.0           3.6            1.4           0.2  Iris-setosa
'''

# Load data
total_df = pd.read_csv("./iris/iris.csv")
total_df.set_index("Id")
total_df = total_df.drop(labels=["Unnamed: 0"], axis=1)
print(total_df.head())


# Drop
total_df = total_df.drop(["Id"], axis=1)
x_data = total_df.drop(["Species"], axis=1)
y_data = total_df["Species"]


# MinMaxScale
min_max_scaler = StandardScaler()
min_max_scaler.fit(x_data)
# print(x_data.head())
x_data = min_max_scaler.transform(x_data)
print(f"x_data: {x_data.shape}")


# Label Encoder
label_enc = LabelEncoder()
label_enc.fit(y_data)
# print(y_data.head())
y_data = label_enc.transform(y_data)
print(f"y_data: {y_data.shape}")


# Split Train, Test
train_x, test_x, train_y, test_y = train_test_split(
    x_data, y_data, test_size=0.2, random_state=42, stratify=y_data
)
print(f"Train - x: {train_x.shape}, y: {train_y.shape}")
print(f"Test - x: {test_x.shape}, y: {test_y.shape}")


# Hyperparameter
param_grids = {
    "n_estimators": [100, 200],
    "learning_rate": [0.01, 0.1, 0.3],
    "max_depth": [3, 6]
}
grid_search = GridSearchCV(
    xgb.XGBClassifier(),
    param_grids,
    cv=5,
    n_jobs=-1,
    scoring="accuracy"
)
grid_search.fit(train_x, train_y)
best_params = grid_search.best_params_
print(f"best_params: {best_params}")

# Model
model_1 = RandomForestClassifier()
model_2 = xgb.XGBClassifier(**best_params)
model_3 = LogisticRegression()
model_4 = KNeighborsClassifier()
model_5 = Lasso()

model_1.fit(train_x, train_y)
model_2.fit(train_x, train_y)
model_3.fit(train_x, train_y)
model_4.fit(train_x, train_y)
model_5.fit(train_x, train_y)

# Valid
# print(model_1.score(train_x, train_y))
# print(model_2.score(train_x, train_y))
# print(model_3.score(train_x, train_y))
# print(model_4.score(train_x, train_y))
# print(model_5.score(train_x, train_y))

# Test
print(model_1.score(test_x, test_y))
print(model_2.score(test_x, test_y))
print(model_3.score(test_x, test_y))
print(model_4.score(test_x, test_y))
print(model_5.score(test_x, test_y))

# sample
predict_x = np.array([
    [5.3, 3.7, 1.5, 0.2]
])
answer = predict_x.copy()
answer = pd.DataFrame(answer, columns=["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"])

predict_x = min_max_scaler.transform(predict_x)

predict_1 = label_enc.inverse_transform(model_1.predict(predict_x))
predict_2 = label_enc.inverse_transform(model_2.predict(predict_x))
predict_3 = label_enc.inverse_transform(model_3.predict(predict_x))
predict_4 = label_enc.inverse_transform(model_4.predict(predict_x))
# predict_5 = label_enc.inverse_transform(model_5.predict(predict_x))

# print(f"predict - 1: {predict_1}, 2: {predict_2}, 3: {predict_3}, 4: {predict_4}, 5: {predict_5}")

answer["Species"] = predict_4
print(answer)