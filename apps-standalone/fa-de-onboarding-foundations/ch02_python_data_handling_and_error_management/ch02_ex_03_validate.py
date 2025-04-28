def validate_product(product, prefix):  # Takes product and prefix
    """Validate product prefix."""
    cleaned = product.strip()  # Clean string
    is_valid = cleaned.startswith(prefix)  # Check prefix
    if not is_valid:  # Debug if validation fails
        print(f"Debug: Cleaned product is '{cleaned}'")  # Print cleaned product
    print(f"Validating {product}: {is_valid}")  # Debug
    return is_valid  # Return result


# Test
print(validate_product("Halal Laptop", "Halal"))  # Call function

# Output:
# Validating Halal Laptop: True
# True
