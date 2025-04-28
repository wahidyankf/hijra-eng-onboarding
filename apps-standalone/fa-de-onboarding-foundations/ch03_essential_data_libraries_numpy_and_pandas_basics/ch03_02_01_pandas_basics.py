import pandas as pd  # Import Pandas with standard alias

# Load sales CSV
df = pd.read_csv("data/sales.csv")  # Read CSV into DataFrame

# Inspect DataFrame
print("DataFrame Head:")  # Debug: print first few rows
print(df.head())  # Show first 5 rows
print("DataFrame Info:")  # Debug: print structure
print(df.info())  # Show column types and null counts

# Expected Output (with sales.csv from Appendix 1):
# DataFrame Head:
#          product   price  quantity
# 0   Halal Laptop  999.99         2
# 1    Halal Mouse   24.99        10
# 2  Halal Keyboard   49.99         5
# 3            NaN   29.99         3
# 4       Monitor      NaN         2
# DataFrame Info:
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 6 entries, 0 to 5
# Data columns (total 3 columns):
#  #   Column    Non-Null Count  Dtype
# ---  ------    --------------  -----
#  0   product   5 non-null      object
#  1   price     5 non-null      float64
#  2   quantity  6 non-null      int64
# dtypes: float64(1), int64(1), object(1)
# memory usage: 272.0+ bytes
