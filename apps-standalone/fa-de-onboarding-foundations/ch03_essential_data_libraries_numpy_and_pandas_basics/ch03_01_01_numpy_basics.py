import numpy as np  # Import NumPy with standard alias

# Create arrays from sales data
prices = np.array([999.99, 24.99, 49.99])  # Array of prices
quantities = np.array([2, 10, 5])  # Array of quantities

# Vectorized operations
amounts = prices * quantities  # Element-wise multiplication
total_sales = np.sum(amounts)  # Sum all amounts
average_price = np.mean(prices)  # Average price
max_quantity = np.max(quantities)  # Maximum quantity

# Print results
print("Prices:", prices)  # Debug: print array
print("Quantities:", quantities)  # Debug: print array
print("Amounts:", amounts)  # Debug: print computed amounts
print("Total Sales:", total_sales)  # Output total
print("Average Price:", average_price)  # Output average
print("Max Quantity:", max_quantity)  # Output max

# Expected Output:
# Prices: [999.99  24.99  49.99]
# Quantities: [2 10  5]
# Amounts: [1999.98  249.9   249.95]
# Total Sales: 2499.83
# Average Price: 358.3233333333333
# Max Quantity: 10
