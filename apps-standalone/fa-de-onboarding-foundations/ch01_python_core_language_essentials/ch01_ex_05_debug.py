total_sales = 0


def add_sale(price, quantity):  # Fix: Use global variable
    """Add sale to global total."""
    global total_sales  # Declare global
    total_sales = price * quantity  # Update global
    print("Amount:", total_sales)  # Print amount


add_sale(999.99, 2)
print("Total Sales:", total_sales)

# Output:
# Amount: 1999.98
# Total Sales: 1999.98
