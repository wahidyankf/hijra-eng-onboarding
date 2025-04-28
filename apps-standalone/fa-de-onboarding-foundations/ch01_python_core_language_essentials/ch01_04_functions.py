def calculate_amount(price, quantity):  # Define function
    """Calculate sale amount."""
    print("Calculating:", price, quantity)  # Debug
    return price * quantity  # Return product


# Call function
amount = calculate_amount(999.99, 2)  # Call with arguments
print("Amount:", amount)  # Output result

# Expected Output:
# Calculating: 999.99 2
# Amount: 1999.98
