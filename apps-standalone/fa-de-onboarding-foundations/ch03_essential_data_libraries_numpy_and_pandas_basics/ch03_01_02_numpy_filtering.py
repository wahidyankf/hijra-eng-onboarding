import numpy as np  # Import NumPy

# Create arrays
quantities = np.array([2, 10, 5, 150])  # Sales quantities
prices = np.array([999.99, 24.99, 49.99, 5.00])  # Prices

# Filter high-quantity sales (>100)
high_quantity = quantities > 100  # Boolean array
filtered_prices = prices[high_quantity]  # Filter prices where quantities > 100

# Print results
print("Quantities:", quantities)  # Debug: print quantities
print("High Quantity Mask:", high_quantity)  # Debug: print boolean mask
print("Filtered Prices:", filtered_prices)  # Output filtered prices

# Expected Output:
# Quantities: [  2  10   5 150]
# High Quantity Mask: [False False False  True]
# Filtered Prices: [5.]
