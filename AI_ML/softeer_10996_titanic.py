import pandas as pd

from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_transformer
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.svm import SVC

# Load Data
train_df = pd.read_csv("titanic/train.csv")
test_df = pd.read_csv("titanic/test.csv")

# Train Data
x_train = train_df[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Cabin', 'Embarked']]
y_train = train_df['Survived']

# Test Data
x_test = test_df[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Cabin', 'Embarked']]

# NaN
# print(x_train.isnull().sum())

x_train.loc[:, 'Cabin'] = x_train['Cabin'].fillna("Unknown").apply(lambda x:x[0])
x_test.loc[:, 'Cabin'] = x_test['Cabin'].fillna("Unknown").apply(lambda x:x[0])

most_common_embarked = x_train["Embarked"].mode()[0] # 최빈값
x_train.loc[:, 'Embarked'] = x_train['Embarked'].fillna(most_common_embarked)
x_test.loc[:, 'Embarked'] = x_test['Embarked'].fillna(most_common_embarked)

midian_age = x_train["Age"].median() # 중앙값
x_train.loc[:, "Age"] = x_train["Age"].fillna(midian_age)
x_test.loc[:, "Age"] = x_test["Age"].fillna(midian_age)


# 나이를 그룹화
x_train.loc[:, "AgeGroup"] = pd.cut(x_train["Age"], bins=[0, 12, 18, 30, 50, 80], labels=[0, 1, 2, 3, 4])
x_test.loc[:, "AgeGroup"] = pd.cut(x_test["Age"], bins=[0, 12, 18, 30, 50, 80], labels=[0, 1, 2, 3, 4])
# 기존 Age 컬럼 제거
x_train = x_train.drop(columns=['Age'])
x_test = x_test.drop(columns=['Age'])

midian_fare = x_train["Fare"].median() # 중앙값
x_train.loc[:, "Fare"] = x_train["Fare"].fillna(midian_fare)
x_test.loc[:, "Fare"] = x_test["Fare"].fillna(midian_fare)

# 운임을 그룹화
x_train.loc[:, "FareGroup"] = pd.qcut(x_train["Fare"], q=4, labels=[0, 1, 2, 3])
x_test.loc[:, "FareGroup"] = pd.qcut(x_test["Fare"], q=4, labels=[0, 1, 2, 3])

# 기존 Fare 컬럼 제거
x_train = x_train.drop(columns=['Fare'])
x_test = x_test.drop(columns=['Fare'])

# 가족 크기 추가 (SibSp + Parch + 본인)
x_train.loc[:, "FamilySize"] = x_train["SibSp"] + x_train["Parch"] + 1
x_test.loc[:, "FamilySize"] = x_test["SibSp"] + x_test["Parch"] + 1

# 기존 SibSp, Parch 컬럼 제거
x_train = x_train.drop(columns=['SibSp', 'Parch'])
x_test = x_test.drop(columns=['SibSp', 'Parch'])

print(x_train.isnull().sum())
print(x_test.isnull().sum())

# OneHot
transformer = make_column_transformer(
    (OneHotEncoder(handle_unknown='ignore', sparse_output=False), ['Sex', "Cabin", "Embarked"]),
    remainder='passthrough'
)
pipeline = make_pipeline(transformer, MinMaxScaler())

x_train = pipeline.fit_transform(x_train)
x_test = pipeline.transform(x_test)

# print(x_train)

# 하이퍼파라미터 후보
param_grid = {
    'C': [0.1, 1, 10, 100], 
    'gamma': [0.001, 0.01, 0.1, 1, 'scale', 'auto'], 
    'kernel': ['rbf', 'poly']
}

grid = GridSearchCV(SVC(probability=True), param_grid, cv=5, scoring='accuracy', n_jobs=-1)
grid.fit(x_train, y_train)

print("최적 하이퍼파라미터:", grid.best_params_)

# Model
# model = DecisionTreeRegressor()
# model = SVC(kernel='rbf', C=1.0, gamma="auto", probability=True)
model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
model.fit(x_train, y_train)

# Prediction
y_pred = model.predict(x_test)

# print(y_pred)

survived_vals = (y_pred >= 0.5).astype(int)
test_df.insert(0,"Survived", survived_vals)
test_df.to_csv("titanic/answer.csv", index=False)