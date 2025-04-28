# Global variable
total_sales = 0


def add_sale(price, quantity):  # Define function
    """Add sale to global total."""
    global total_sales  # Access global
    amount = price * quantity  # Local variable
    total_sales += amount  # Update global
    print("Local Amount:", amount)  # Debug: print local
    print("Global Total:", total_sales)  # Debug: print global


# Call function
add_sale(999.99, 2)  # Add sale
print("Final Total:", total_sales)  # Output final total

# Expected Output:
# Local Amount: 1999.98
# Global Total: 1999.98
# Final Total: 1999.98
