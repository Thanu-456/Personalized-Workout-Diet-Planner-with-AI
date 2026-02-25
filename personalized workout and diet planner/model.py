# model.py
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
data = {
    "calorie_intake": [1800, 2200, 2500, 2000, 2700, 1500, 2300],
    "activity_level": [1.2, 1.5, 1.7, 1.3, 1.8, 1.1, 1.6],
    "weight": [70, 80, 65, 75, 85, 60, 90],
    "weekly_weight_change": [-0.5, 0.3, 0.6, -0.2, 0.7, -0.8, 0.2]
}

df = pd.DataFrame(data)

X = df[["calorie_intake", "activity_level", "weight"]]
y = df["weekly_weight_change"]

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "weight_model.pkl")

print("Model Trained & Saved Successfully")