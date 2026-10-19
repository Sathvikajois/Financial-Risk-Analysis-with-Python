# ==========================================
# TASK 1: DATA CLEANING AND FORMATTING
# ==========================================

# Import libraries
import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("morgan_stanely.csv")

# ==========================================
# Initial Data Exploration
# ==========================================

# Display first 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Dataset shape
print("\nDataset Shape:")
print(df.shape)

# Column names
print("\nColumn Names:")
print(df.columns)

# Dataset information
print("\nDataset Information:")
df.info()

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# ==========================================
# Check Unique Values in Categorical Columns
# ==========================================

print("\nUnique Account Types:")
print(df["AccountType"].unique())

print("\nUnique Transaction Types:")
print(df["TransactionType"].unique())

print("\nUnique Products:")
print(df["Product"].unique())

print("\nUnique Regions:")
print(df["Region"].unique())

# ==========================================
# Check Data Types
# ==========================================

print("\nData Types:")
print(df.dtypes)

# ==========================================
# Convert TransactionDate to Datetime
# ==========================================

df["TransactionDate"] = pd.to_datetime(
    df["TransactionDate"],
    dayfirst=True
)

print("\nTransactionDate converted successfully!")

print(df["TransactionDate"].head())

print("\nTransactionDate Data Type:")
print(df["TransactionDate"].dtype)

# ==========================================
# Save Cleaned Dataset
# ==========================================

df.to_csv("cleaned_morgan_stanely.csv", index=False)

print("\nCleaned dataset saved successfully!")