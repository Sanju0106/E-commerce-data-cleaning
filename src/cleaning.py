import pandas as pd

# Load dataset
df = pd.read_excel("data/raw/Dataset for Data Analytics.xlsx")

# Display first 5 rows
print(df.head())

# Check dataset informaion
df.info()

# Null Count
print(df.isna().sum())

# Duplicate Count
print("Duplicate Count : ", df.duplicated().sum())

# Checking Unique Values for Categorical Columns
categorical_columns = [
    "Product",
    "PaymentMethod",
    "OrderStatus",
    "CouponCode",
    "ReferralSource"
]

for i in categorical_columns:
    print(f"\nUnique values in {i}:")
    print(df[i].unique())

# Check Numerical Columns
print(df.describe())

# Handling Null Values
df["CouponCode"] = df["CouponCode"].fillna("No Coupon")

# Checking Null Values After Cleaning
print(df["CouponCode"].isna().sum())