import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_excel("Sample data (1).xlsx")
df.columns = df.columns.str.strip()
df["Discount Band"] = df["Discount Band"].fillna("Unknown")
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# EDA
print(df.info())
print(df.describe(include="all"))
print(df.isna().sum())
print(df.groupby("Country")["Sales"].sum().sort_values(ascending=False))
print(df.groupby("Product")["Sales"].sum().sort_values(ascending=False))
print(df.groupby("Segment")["Sales"].sum().sort_values(ascending=False))

# Regression to predict Sales.
# Gross Sales, Discounts and COGS are excluded because they are direct sales-related components.
df["Date_Month"] = df["Date"].dt.month
features = ["Segment","Country","Product","Discount Band","Units Sold",
            "Manufacturing Price","Sale Price","Month Number","Year","Date_Month"]
X = df[features]
y = df["Sales"]

cat = ["Segment","Country","Product","Discount Band"]
num = [c for c in features if c not in cat]

pre = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown="ignore"), cat),
    ("num", "passthrough", num)
])
model = Pipeline([("preprocessor", pre), ("regressor", LinearRegression())])

train_idx, test_idx = train_test_split(np.arange(len(df)), test_size=0.20, random_state=42)
model.fit(X.iloc[train_idx], y.iloc[train_idx])
pred = model.predict(X.iloc[test_idx])

print("R2:", r2_score(y.iloc[test_idx], pred))
print("MAE:", mean_absolute_error(y.iloc[test_idx], pred))
print("RMSE:", mean_squared_error(y.iloc[test_idx], pred) ** 0.5)
