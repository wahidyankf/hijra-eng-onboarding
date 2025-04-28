def calculate_amount(price, quantity):  # Takes price and quantity
    """Calculate sale amount."""
    print("Calculating:", price, quantity)  # Debug
    return price * quantity  # Return product


# Test
print(calculate_amount(999.99, 2))  # Call function

# Output:
# Calculating: 999.99 2
# 1999.98
