import numpy as np  # Import NumPy


def calculate_sales(prices, quantities):  # Takes prices and quantities lists
    """Compute total sales using NumPy."""
    if (
        not prices or not quantities or len(prices) != len(quantities)
    ):  # Check for empty or mismatched inputs
        return 0.0  # Return 0 for invalid input
    if any(q < 0 for q in quantities):  # Check for negative quantities
        print("Error: Negative quantities detected")  # Log error
        return 0.0  # Return 0 for invalid input
    prices_array = np.array(prices)  # Convert to array
    quantities_array = np.array(quantities)  # Convert to array
    amounts = prices_array * quantities_array  # Compute amounts
    total = np.sum(amounts)  # Sum amounts
    print("Amounts:", amounts)  # Debug
    return total  # Return total


# Test
print(calculate_sales([999.99, 24.99, 49.99], [2, 10, 5]))  # Call function

# Output:
# Amounts: [1999.98  249.9   249.95]
# 2499.83
