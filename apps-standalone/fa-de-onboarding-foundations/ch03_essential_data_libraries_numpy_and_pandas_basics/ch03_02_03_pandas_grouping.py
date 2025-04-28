import pandas as pd  # Import Pandas

# Load and clean DataFrame
df = pd.read_csv("data/sales.csv")  # Read CSV
df = df.dropna(subset=["product", "price"])  # Drop missing product/price
df = df[df["product"].str.startswith("Halal")]  # Filter Halal products

# Compute amount per sale
df["amount"] = df["price"] * df["quantity"]  # New column for price * quantity

# Group by product and sum amounts
sales_by_product = df.groupby("product")["amount"].sum()  # Returns a Series

# Print results
print("Sales by Product (Series):")  # Debug
print(sales_by_product)  # Show grouped sums

# Expected Output:
# Sales by Product (Series):
# product
# Halal Keyboard     249.95
# Halal Laptop      1999.98
# Halal Mouse        249.90
# Name: amount, dtype: float64
