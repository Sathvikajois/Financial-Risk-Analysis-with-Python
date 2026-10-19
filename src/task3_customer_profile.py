import pandas as pd

# Load cleaned dataset
df = pd.read_csv("cleaned_morgan_stanely.csv")

# Customer Profile Building

customer_profile = df.groupby("AccountID").agg(
    TransactionFrequency=("TransactionID", "count"),
    AverageBalance=("AccountBalance", "mean"),
    TotalTransactionAmount=("TransactionAmount", "sum")
).reset_index()

# Activity Level Rubric

def activity_level(x):
    if x >= 5:
        return "High Activity"
    elif x >= 3:
        return "Medium Activity"
    else:
        return "Low Activity"

customer_profile["ActivityLevel"] = customer_profile[
    "TransactionFrequency"
].apply(activity_level)

print("\nActivity Level Summary")
print(customer_profile["ActivityLevel"].value_counts())

# Balance Segmentation

customer_profile["BalanceSegment"] = pd.qcut(
    customer_profile["AverageBalance"],
    q=3,
    labels=["Low Balance", "Medium Balance", "High Balance"]
)

print("\nBalance Segments")
print(customer_profile["BalanceSegment"].value_counts())

# Transaction Volume Segmentation

customer_profile["TransactionVolume"] = pd.qcut(
    customer_profile["TotalTransactionAmount"],
    q=3,
    labels=["Low Volume", "Medium Volume", "High Volume"]
)

print("\nTransaction Volume")
print(customer_profile["TransactionVolume"].value_counts())

# High Net Inflow Accounts

high_inflow = customer_profile.sort_values(
    by="TotalTransactionAmount",
    ascending=False
).head(10)

print("\nTop 10 High Net Inflow Accounts")
print(high_inflow)

# High Frequency Low Balance

high_freq_low_balance = customer_profile[
    (customer_profile["ActivityLevel"] == "High Activity") &
    (customer_profile["BalanceSegment"] == "Low Balance")
]

print("\nHigh Frequency Low Balance Accounts")
print(high_freq_low_balance)

# Negative or Near Zero Balance

negative_balance = customer_profile[
    customer_profile["AverageBalance"] <= 1000
]

print("\nNegative / Near Zero Balance Accounts")
print(negative_balance)

# Save Result

customer_profile.to_csv(
    "customer_profile_summary.csv",
    index=False
)

print("\nCustomer Profile Summary saved successfully!")