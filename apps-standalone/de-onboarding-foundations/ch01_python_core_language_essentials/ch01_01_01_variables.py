# Variables for a Sharia-compliant sale
product_name = "Halal Laptop"  # str: product name
price = 999.99  # float: price in dollars
quantity = 2  # int: number of units
is_sharia_compliant = True  # bool: Sharia compliance flag

# Print variables
print("Product:", product_name)  # Debug: print product
print("Price:", price)  # Debug: print price
print("Quantity:", quantity)  # Debug: print quantity
print("Sharia Compliant:", is_sharia_compliant)  # Debug: print boolean

# Validate Halal prefix and calculate profit margin
if product_name.startswith("Halal"):
    profit_margin = price * 0.1  # 10% margin
    print("Profit Margin:", profit_margin)  # Debug: print margin

# Expected Output:
# Product: Halal Laptop
# Price: 999.99
# Quantity: 2
# Sharia Compliant: True
# Profit Margin: 99.999
