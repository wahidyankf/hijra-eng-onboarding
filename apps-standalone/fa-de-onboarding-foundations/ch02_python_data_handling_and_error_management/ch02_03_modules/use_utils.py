import utils  # Import utils module

# Use module functions
product = "  Halal Laptop  "  # Product with whitespace
cleaned = utils.clean_string(product)  # Clean string
price = "999.99"  # Price string
is_valid = utils.is_numeric(price, max_decimals=2)  # Validate price

# Print results
print("Cleaned Product:", cleaned)  # Debug
print("Is Valid Price:", is_valid)  # Debug

# Expected Output:
# Cleaned Product: Halal Laptop
# Is Valid Price: True
