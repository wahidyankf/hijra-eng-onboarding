import pandas as pd  # Import Pandas


def group_sales(csv_path):  # Takes CSV path
    """Group sales by product and compute totals."""
    df = pd.read_csv(csv_path)  # Load CSV
    df["amount"] = df["price"] * df["quantity"]  # Compute amount
    sales_by_product = df.groupby("product")["amount"].sum()  # Fix: Group by product
    return sales_by_product  # Return Series


# Test
print(group_sales("data/sample.csv"))  # Call function

# Output:
# product
# Halal Laptop    1999.98
# Halal Mouse      249.90
# Name: amount, dtype: float64
