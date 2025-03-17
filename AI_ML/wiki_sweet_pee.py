import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestRegressor

# Load Data
train_df = pd.read_csv("./sweet_pee/sweet_pee_train.csv")
test_df = pd.read_csv("./sweet_pee/sweet_pee_test.csv")

'''
    ID   임신  글루코스(탄수화물 화합물)    혈압  피부두께    인슐린   BMI  가족력    나이  당뇨여부
0  1.0  6.0           148.0  72.0  35.0    0.0  33.6  0.6  50.0   1.0
1  3.0  1.0            89.0  66.0  23.0   94.0  28.1  0.2  21.0   0.0
2  4.0  0.0           137.0  40.0  35.0  168.0  43.1  2.3  33.0   1.0
3  6.0  2.0           197.0  70.0  45.0  543.0  30.5  0.2  53.0   1.0
4  8.0  5.0           166.0  72.0  19.0  175.0  25.8  0.6  51.0   1.0
'''
print(train_df.head())

# Split Data
x_train = train_df.drop(["ID", "당뇨여부"], axis=1)
y_train = train_df["당뇨여부"]

x_test = test_df.drop(["ID", "당뇨여부"], axis=1)
y_test = test_df["당뇨여부"]

# Check NaN
print(x_train.isnull().sum())
print(x_test.isnull().sum())

# Model
model = LogisticRegression()
model.fit(x_train, y_train)

# Valid
print(model.score(x_train, y_train))


# Prediction
preds = model.predict(x_test)

preds_df = pd.DataFrame({
    "당뇨여부": preds
})

preds_df.loc[:, "당뇨여부"] = np.where(preds_df["당뇨여부"] >= 0.5, "당뇨", "정상")
print(preds_df)