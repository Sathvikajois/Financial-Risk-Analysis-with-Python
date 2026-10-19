import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("cleaned_morgan_stanely.csv")

# Convert TransactionDate back to datetime
df["TransactionDate"] = pd.to_datetime(df["TransactionDate"])

# Display first 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Dataset shape
print("\nDataset Shape:")
print(df.shape)
# Extract Month and Year
df["Month"] = df["TransactionDate"].dt.month_name()
df["Year"] = df["TransactionDate"].dt.year

print("\nMonths in Dataset:")
print(df["Month"].unique())

print("\nYears in Dataset:")
print(df["Year"].unique())

# Monthly Transaction Analysis

month_order = [
    "January","February","March","April","May","June",
    "July","August","September","October","November","December"
]

monthly_transactions = (
    df.groupby("Month")["TransactionAmount"]
      .sum()
      .reindex(month_order)
)

print("\nMonthly Transaction Totals:")
print(monthly_transactions)

# Line Chart - Monthly Transaction Totals

plt.figure(figsize=(10,5))

plt.plot(month_order,
         monthly_transactions,
         marker='o')

plt.title("Monthly Transaction Totals")
plt.xlabel("Month")
plt.ylabel("Transaction Amount")

plt.xticks(rotation=45)

plt.grid(True)

plt.tight_layout()

plt.show()

# Yearly Transaction Summary

yearly_transactions = df.groupby("Year")["TransactionAmount"].sum()

print("\nYearly Transaction Totals:")
print(yearly_transactions)

# Yearly Transaction Chart

plt.figure(figsize=(6,5))

plt.bar(yearly_transactions.index.astype(str),
        yearly_transactions.values)

plt.title("Yearly Transaction Totals")
plt.xlabel("Year")
plt.ylabel("Transaction Amount")

plt.tight_layout()

plt.show()

# Yearly Transaction Summary

yearly_transactions = df.groupby("Year")["TransactionAmount"].sum()

print("\nYearly Transaction Totals:")
print(yearly_transactions)

