import pandas as pd

import utils  # Import utils module

# Load and clean DataFrame
df = pd.read_csv("data/sales.csv")  # Read CSV
df = df.dropna(subset=["product"])  # Drop rows with missing product
df = df[df["product"].str.startswith("Halal")]  # Filter Halal products
df = df[df["quantity"] <= 100]  # Filter quantity <= 100

df = df[df["price"].apply(utils.is_numeric)]  # type: ignore  # Ensure price is numeric

# Print cleaned DataFrame
print("Cleaned DataFrame:")  # Debug
print(df)  # Show filtered DataFrame

# Expected Output:
# Cleaned DataFrame:
#          product   price  quantity
# 0   Halal Laptop  999.99         2
# 1    Halal Mouse   24.99        10
# 2  Halal Keyboard   49.99         5
