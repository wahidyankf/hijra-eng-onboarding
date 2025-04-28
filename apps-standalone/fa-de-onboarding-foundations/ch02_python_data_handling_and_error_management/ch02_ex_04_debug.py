def validate_price(price):  # Takes price string
    """Validate price as decimal number."""
    parts = price.split(".")  # Split on decimal
    is_valid = (
        len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit()
    )  # Check format
    print(f"Validating {price}: {is_valid}")  # Debug
    return is_valid  # Return result


# Test
print(validate_price("999.99"))  # Call function

# Output:
# Validating 999.99: True
# True
