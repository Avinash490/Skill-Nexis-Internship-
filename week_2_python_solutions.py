# Week 2 Practice Set — Python for Data Analysis
import pandas as pd

# CSV version:
# df = pd.read_csv("sales.csv")

# Supplied dataset is Excel:
df = pd.read_excel("SQL_Sales_Dataset_200_Rows.xlsx")

# 1. Basic information
print(df.head())
print(df.info())
print(df.shape)
print(df.describe(include="all"))

# 2. Missing values and duplicates
print(df.isna().sum())
print("Duplicate rows:", df.duplicated().sum())
df = df.drop_duplicates()

# 3. Total revenue by category
revenue_by_category = (
    df.groupby("category", as_index=False)["total_price"]
      .sum()
      .sort_values("total_price", ascending=False)
)
print(revenue_by_category)

# 4. Sort by multiple columns
sorted_df = df.sort_values(
    by=["region", "total_price"],
    ascending=[True, False]
)
print(sorted_df[["region", "category", "total_price"]].head(10))

# 5. Correlation matrix
numeric_df = df.select_dtypes(include="number")
correlation_matrix = numeric_df.corr()
print(correlation_matrix.round(3))

# Extra Week 2 analysis: top customers and average order value
top_customers = (
    df.groupby("customer_name")
      .agg(
          total_revenue=("total_price", "sum"),
          order_count=("order_id", "nunique"),
          average_order_value=("total_price", "mean")
      )
      .sort_values("total_revenue", ascending=False)
      .head(10)
)
print(top_customers)

print("Overall average order value:", df["total_price"].mean())
