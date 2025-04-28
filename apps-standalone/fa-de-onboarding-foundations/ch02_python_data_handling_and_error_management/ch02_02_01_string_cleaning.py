# Clean a string
text = "  Halal Laptop  "  # String with whitespace
cleaned = text.strip()  # Remove leading/trailing whitespace
print("Cleaned:", cleaned)  # Debug: print result

# Validate numeric string
price = "999.99"  # Price string
is_numeric = price.replace(".", "", 1).isdigit()  # Check if numeric (one decimal)
print("Is Numeric:", is_numeric)  # Debug: print result

# Expected Output:
# Cleaned: Halal Laptop
# Is Numeric: True
