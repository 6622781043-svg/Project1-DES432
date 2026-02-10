# ==============================
# Project 1: Online Buying and Selling
# Exploratory Data Analysis & Inference
# ==============================

from google.colab import files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
# 1) Upload & Load Dataset
# ------------------------------
uploaded = files.upload()
df = pd.read_csv(list(uploaded.keys())[0])

print("Dataset loaded successfully")
print("Shape:", df.shape)

# ------------------------------
# 2) Check Missing Values (BEFORE cleaning)
# ------------------------------
print("\nMissing values BEFORE cleaning:")
print(df.isna().sum())

print("\nPercentage of missing values (%):")
print((df.isna().sum() / len(df)) * 100)

# Keep raw dataset for transparency
df_raw = df.copy()

# ------------------------------
# 3) Data Cleaning
# ------------------------------
# Numerical → median
df["customer_age"] = df["customer_age"].fillna(df["customer_age"].median())
df["delivery_days"] = df["delivery_days"].fillna(df["delivery_days"].median())

# Categorical → 'Unknown'
df["gender"] = df["gender"].fillna("Unknown")

print("\nMissing values AFTER cleaning:")
print(df.isna().sum())

# ------------------------------
# 4) Exploratory Data Analysis
# ------------------------------
# Distribution of order value
plt.figure()
plt.hist(df["order_value"], bins=30)
plt.xlabel("Order Value")
plt.ylabel("Frequency")
plt.title("Distribution of Order Value")
plt.show()

# Order value by product category
plt.figure()
df.boxplot(column="order_value", by="product_category")
plt.xlabel("Product Category")
plt.ylabel("Order Value")
plt.title("Order Value by Product Category")
plt.suptitle("")
plt.show()

# Delivery days by return status
plt.figure()
df.boxplot(column="delivery_days", by="returned")
plt.xlabel("Returned")
plt.ylabel("Delivery Days")
plt.title("Delivery Days by Return Status")
plt.suptitle("")
plt.show()

# ------------------------------
# 5) Descriptive Statistics
# ------------------------------
print("\nDescriptive Statistics:")
print(df[["customer_age", "order_value", "delivery_days"]].describe())

iqr = df["order_value"].quantile(0.75) - df["order_value"].quantile(0.25)
print("IQR of Order Value:", iqr)

# ------------------------------
# 6) Statistical Inference
# ------------------------------
# 95% Confidence Interval for mean order value
mean_val = df["order_value"].mean()
std_val = df["order_value"].std()
n = len(df)
z = 1.96

ci_low = mean_val - z * (std_val / np.sqrt(n))
ci_high = mean_val + z * (std_val / np.sqrt(n))

print("\n95% Confidence Interval for Mean Order Value:")
print((ci_low, ci_high))

# Mean comparison: returned vs not returned
returned = df[df["returned"] == "Yes"]["delivery_days"]
not_returned = df[df["returned"] == "No"]["delivery_days"]

mean_diff = returned.mean() - not_returned.mean()

print("\nMean delivery days (Returned):", returned.mean())
print("Mean delivery days (Not Returned):", not_returned.mean())
print("Mean difference:", mean_diff)

print("\nAnalysis completed successfully.")
