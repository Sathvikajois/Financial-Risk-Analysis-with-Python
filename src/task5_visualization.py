import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("cleaned_morgan_stanely.csv")

# Convert date column
df["TransactionDate"] = pd.to_datetime(df["TransactionDate"])

# Chart 1 - Transaction Type

plt.figure(figsize=(6,4))
df["TransactionType"].value_counts().plot(kind="bar")
plt.title("Transaction Type Distribution")
plt.xlabel("Transaction Type")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# Chart 2 - Account Type

plt.figure(figsize=(6,4))
df["AccountType"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Account Type Distribution")
plt.tight_layout()
plt.show()

# Chart 3 - Region-wise Transaction Amount

region = df.groupby("Region")["TransactionAmount"].sum()

plt.figure(figsize=(7,4))
region.plot(kind="bar")
plt.title("Region-wise Transaction Amount")
plt.xlabel("Region")
plt.ylabel("Transaction Amount")
plt.tight_layout()
plt.show()

# Chart 4 - Product-wise Transaction Amount

product = df.groupby("Product")["TransactionAmount"].sum()

plt.figure(figsize=(8,4))
product.plot(kind="bar")
plt.title("Product-wise Transaction Amount")
plt.xlabel("Product")
plt.ylabel("Transaction Amount")
plt.tight_layout()
plt.show()

# Chart 5 - Risk Score Distribution

plt.figure(figsize=(6,4))
plt.hist(df["RiskScore"], bins=15)
plt.title("Risk Score Distribution")
plt.xlabel("Risk Score")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Chart 6 - Credit Rating Distribution

plt.figure(figsize=(6,4))
plt.hist(df["CreditRating"], bins=15)
plt.title("Credit Rating Distribution")
plt.xlabel("Credit Rating")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Chart 7 - Account Balance Distribution

plt.figure(figsize=(6,4))
plt.hist(df["AccountBalance"], bins=20)
plt.title("Account Balance Distribution")
plt.xlabel("Account Balance")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Chart 8 - Top 10 Managers

manager = (
    df.groupby("Manager")["TransactionAmount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(8,4))
manager.plot(kind="bar")
plt.title("Top 10 Managers by Transaction Amount")
plt.xlabel("Manager")
plt.ylabel("Transaction Amount")
plt.tight_layout()
plt.show()

print("Task 5 completed successfully!")