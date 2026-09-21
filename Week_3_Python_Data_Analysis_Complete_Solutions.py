import pandas as pd
import matplotlib.pyplot as plt

# 1. Load data
df = pd.read_csv("global_superstore_2016.csv")
print(df.head())
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
df.info()

# 2. Clean missing values and duplicates
print("Missing values before cleaning:")
print(df.isnull().sum())
print("Duplicates before cleaning:", df.duplicated().sum())

df = df.drop_duplicates().copy()

numeric_cols = df.select_dtypes(include="number").columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

text_cols = df.select_dtypes(include="object").columns
df[text_cols] = df[text_cols].fillna("Unknown")

print("Missing values after cleaning:")
print(df.isnull().sum())
print("Duplicates after cleaning:", df.duplicated().sum())

# 3. Total revenue by category
category_revenue = (
    df.groupby("Category", as_index=False)["Sales"]
      .sum()
      .rename(columns={"Sales": "Total Revenue"})
      .sort_values("Total Revenue", ascending=False)
)
print(category_revenue)

# 4. Sort by multiple columns
sorted_df = df.sort_values(
    by=["Category", "Sales"],
    ascending=[True, False]
)
print(sorted_df.head(20))

# 5. Correlation matrix
numeric_df = df.select_dtypes(include="number")
correlation_matrix = numeric_df.corr()
print(correlation_matrix)

plt.figure(figsize=(10, 7))
plt.imshow(correlation_matrix, cmap="coolwarm", interpolation="nearest")
plt.colorbar()
plt.xticks(range(len(correlation_matrix.columns)),
           correlation_matrix.columns, rotation=45, ha="right")
plt.yticks(range(len(correlation_matrix.columns)),
           correlation_matrix.columns)
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()
