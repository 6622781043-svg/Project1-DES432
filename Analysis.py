# analysis.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import os

# -----------------------------
# 1. Load Dataset
# -----------------------------
df = pd.read_csv("data/online_shopping_dataset.csv")

print("Initial Dataset Shape:", df.shape)
print(df.head())

# -----------------------------
# 2. Check Missing Values
# -----------------------------
missing_summary = df.isnull().sum()
print("\nMissing Values Summary:")
print(missing_summary)

# -----------------------------
# 3. Data Cleaning
# -----------------------------
# Numerical columns: fill with median
num_cols = ['age', 'order_value', 'delivery_days']
for col in num_cols:
    df[col] = df[col].fillna(df[col].median())

# Categorical columns: fill with mode
cat_cols = ['gender', 'payment_method', 'product_category']
for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# -----------------------------
# 4. Descriptive Statistics
# -----------------------------
desc_stats = df.describe()
print("\nDescriptive Statistics:")
print(desc_stats)

# Create figures folder
os.makedirs("figures", exist_ok=True)

# -----------------------------
# 5. Exploratory Data Analysis
# -----------------------------

# 5.1 Distribution of Order Value
plt.figure()
plt.hist(df['order_value'], bins=20)
plt.xlabel("Order Value")
plt.ylabel("Frequency")
plt.title("Distribution of Order Value")
plt.savefig("figures/order_value_distribution.png")
plt.close()

# 5.2 Boxplot of Order Value by Payment Method
plt.figure()
df.boxplot(column='order_value', by='payment_method')
plt.title("Order Value by Payment Method")
plt.suptitle("")
plt.xlabel("Payment Method")
plt.ylabel("Order Value")
plt.savefig("figures/order_value_by_payment.png")
plt.close()

# 5.3 Scatter Plot: Order Value vs Delivery Days
plt.figure()
plt.scatter(df['delivery_days'], df['order_value'])
plt.xlabel("Delivery Days")
plt.ylabel("Order Value")
plt.title("Order Value vs Delivery Days")
plt.savefig("figures/order_vs_delivery.png")
plt.close()

# -----------------------------
# 6. Statistical Inference
# -----------------------------

# 6.1 Confidence Interval for Mean Order Value
mean_order = df['order_value'].mean()
std_order = df['order_value'].std()
n = len(df)

confidence = 0.95
z = stats.norm.ppf((1 + confidence) / 2)

ci_lower = mean_order - z * (std_order / np.sqrt(n))
ci_upper = mean_order + z * (std_order / np.sqrt(n))

print("\n95% Confidence Interval for Mean Order Value:")
print((ci_lower, ci_upper))

# 6.2 Hypothesis Test: Delivery Days (Male vs Female)
male_days = df[df['gender'] == 'Male']['delivery_days']
female_days = df[df['gender'] == 'Female']['delivery_days']

t_stat, p_value = stats.ttest_ind(male_days, female_days)

print("\nT-test: Delivery Days by Gender")
print("t-statistic:", t_stat)
print("p-value:", p_value)

# -----------------------------
# 7. Conclusion Output
# -----------------------------
if p_value < 0.05:
    print("There is a statistically significant difference in delivery days between genders.")
else:
    print("No statistically significant difference in delivery days between genders.")
