# Validate product prefix
product = "Halal Laptop"  # Product name
prefix = "Halal"  # Required prefix
is_valid = product.startswith(prefix)  # Check prefix
print("Has Prefix:", is_valid)  # Debug: print result

# Validate decimal places
price = "999.99"  # Price string
parts = price.split(".")  # Split on decimal
is_valid_decimal = len(parts) == 2 and len(parts[1]) <= 2  # Check format and decimals
print("Valid Decimals:", is_valid_decimal)  # Debug: print result

# Expected Output:
# Has Prefix: True
# Valid Decimals: True
