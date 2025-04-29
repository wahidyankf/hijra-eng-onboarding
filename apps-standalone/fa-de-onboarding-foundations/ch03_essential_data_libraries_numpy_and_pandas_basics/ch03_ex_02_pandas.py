import pandas as pd  # Import Pandas


def load_halal_sales(csv_path):  # Takes CSV path
    """Load and filter CSV for Halal products."""
    df = pd.read_csv(csv_path)  # Load CSV
    print("Initial DataFrame:")  # Debug
    print(df.head())  # Show first rows
    df = df[df["product"].str.startswith("Halal")]  # Filter Halal products
    return df  # Return filtered DataFrame


# Test
print(load_halal_sales("data/sample.csv"))  # Call function

# Output:
# Initial DataFrame:
#          product   price  quantity
# 0   Halal Laptop  999.99         2
# 1    Halal Mouse   24.99        10
#          product   price  quantity
# 0   Halal Laptop  999.99         2
# 1    Halal Mouse   24.99        10
