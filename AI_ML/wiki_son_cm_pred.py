import pandas as pd
from sklearn.linear_model import LinearRegression

# Load Data
train_df = pd.read_csv("./son/father_son_train.csv")
test_df = pd.read_csv("./son/father_son_test.csv")


# Split X, Y
x_train = train_df.drop("Son", axis=1)
y_train = train_df['Son']
print(x_train.shape, y_train.shape)

print(x_train.head())
print()
print(y_train.head())
print()
print(train_df["Father"])

x_test = test_df.drop("Son", axis=1)
y_test = test_df["Son"]
print(x_test.shape, y_test.shape)

# x_train = x_train.to_numpy()
# y_train = y_train.to_numpy()

# x_test = x_test.to_numpy()
# y_test = y_test.to_numpy()

# NaN
# print(x_train.isnull().sum())
# print(x_test.isnull().sum())

# Model
model = LinearRegression()
model.fit(x_train, y_train)

# Valid
scores = model.score(x_test, y_test)
print(scores)

y_preds = model.predict([[162.789]])
print(y_preds)