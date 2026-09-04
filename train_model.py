import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import joblib

# 1. Train and save the Polynomial Regression model (matching Polynomial_Regression_.ipynb)
csv_path = os.path.join(os.path.dirname(__file__), 'advertising.csv')
df = pd.read_csv(csv_path)
required_columns = ["TV", "Radio", "Newspaper", "Sales"]
df = df[required_columns].dropna().drop_duplicates()

X = df[["TV", "Radio", "Newspaper"]]
y = df["Sales"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

model = Pipeline([
    ("polynomial_features", PolynomialFeatures(degree=2, include_bias=False)),
    ("linear_regression", LinearRegression())
])

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

model_filename = os.path.join(os.path.dirname(__file__), "polynomial_regression_model.pkl")
joblib.dump(model, model_filename)
print(f"Model saved to {model_filename}")
print(f"Performance: R2={r2:.4f}, MAE={mae:.4f}, RMSE={rmse:.4f}")
