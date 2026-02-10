# DES432 Project 1: Online Buying and Selling Data Analysis

## 1. Project Overview
This project is part of the DES432 Statistics and Data Modeling course.  
The objective of this project is to apply exploratory data analysis (EDA) and basic statistical inference techniques to a real-world style dataset related to online buying and selling (e-commerce transactions).

Rather than focusing on prediction or machine learning, this project emphasizes:
- Understanding data structure and quality
- Handling missing values appropriately
- Interpreting descriptive statistics
- Applying basic statistical inference
- Communicating findings clearly and transparently

The project simulates realistic challenges commonly found in real-world datasets, such as missing values, skewed distributions, and group comparisons.

---

## 2. Dataset Description
The dataset used in this project is provided in CSV format:

**File name:**  
`online_shopping_dataset.csv`

Each row in the dataset represents one completed online transaction.  
The dataset contains both numerical and categorical variables, including:

### Numerical Variables
- `customer_age`: Age of the customer
- `order_value`: Total monetary value of the order
- `delivery_days`: Number of days required to deliver the order

### Categorical Variables
- `gender`: Gender of the customer
- `product_category`: Category of the purchased product
- `payment_method`: Method used for payment
- `returned`: Indicates whether the order was returned

The dataset intentionally contains missing values to reflect common issues in real-world data collection, such as incomplete customer profiles or system recording limitations.

---

## 3. Data Quality and Cleaning
Before analysis, the dataset was inspected for missing values and potential data quality issues.

### Missing Values Handling
- Numerical variables (`customer_age`, `delivery_days`) were imputed using the **median**, which is robust to skewed distributions and outliers.
- Categorical variables (e.g., `gender`) were filled with meaningful labels or the most frequent category to preserve all observations.

No observations were removed solely due to missing values.  
This approach helps reduce the risk of sampling bias and maintains consistency with the original dataset.

---

## 4. Exploratory Data Analysis (EDA)
Exploratory data analysis was conducted to understand distributions, variability, and potential relationships between variables.

The EDA process includes:
- Distribution analysis of order values using histograms
- Comparison of order values across different product categories and payment methods using boxplots
- Examination of the relationship between delivery performance and order value using scatter plots

These visualizations help identify patterns such as skewness, variability, and potential group differences that are not easily captured by summary statistics alone.

All generated figures are automatically saved in the `figures/` folder.

---

## 5. Descriptive Statistics
Descriptive statistics were calculated to summarize the central tendency and variability of key numerical variables.

Statistics include:
- Mean, median, and standard deviation
- Minimum and maximum values
- Interquartile range (IQR)

These summaries provide context for interpreting customer behavior and delivery performance in the e-commerce environment.

---

## 6. Statistical Inference
Basic statistical inference techniques were applied to incorporate uncertainty into the analysis.

### Confidence Interval
A 95% confidence interval was constructed for the mean order value to estimate the average spending behavior of customers.

### Hypothesis Testing
A two-sample t-test was conducted to compare average delivery days between different customer groups (e.g., gender groups).

The results help evaluate whether observed differences are likely due to random variation or represent statistically significant patterns.

It is important to note that statistical significance does not imply causality. The analysis focuses on association rather than cause-and-effect relationships.

---

## 7. Project Structure
The repository is organized as follows:

