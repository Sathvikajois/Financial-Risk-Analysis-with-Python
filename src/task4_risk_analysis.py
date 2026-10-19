import pandas as pd

# Load Cleaned Dataset

df = pd.read_csv("cleaned_morgan_stanely.csv")

# 1. Frequent Large Withdrawals

withdrawals = df[
    df["TransactionType"].str.lower() == "withdrawal"
]

large_amount = withdrawals["TransactionAmount"].quantile(0.90)

large_withdrawals = withdrawals[
    withdrawals["TransactionAmount"] >= large_amount
]

frequent_large = (
    large_withdrawals.groupby("AccountID")
    .size()
    .reset_index(name="LargeWithdrawalCount")
)

print("\nFrequent Large Withdrawal Accounts")
print(frequent_large)

# 2. Balance Volatility

volatility = (
    df.groupby("AccountID")["AccountBalance"]
    .std()
    .reset_index(name="BalanceVolatility")
)

print("\nBalance Volatility")
print(volatility.head())

# 3. IQR Anomaly Detection

Q1 = df["TransactionAmount"].quantile(0.25)
Q3 = df["TransactionAmount"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

anomalies = df[
    (df["TransactionAmount"] < lower) |
    (df["TransactionAmount"] > upper)
]

print("\nAnomalies Detected")
print(anomalies)

# 4. High Risk Customers

risk_threshold = df["RiskScore"].quantile(0.90)

high_risk = df[
    df["RiskScore"] >= risk_threshold
]

print("\nHigh Risk Customers")
print(high_risk)

# Save Results

frequent_large.to_csv(
    "large_withdrawal_accounts.csv",
    index=False
)

volatility.to_csv(
    "balance_volatility.csv",
    index=False
)

anomalies.to_csv(
    "transaction_anomalies.csv",
    index=False
)

high_risk.to_csv(
    "high_risk_customers.csv",
    index=False
)

print("\nRisk Analysis Completed Successfully!")