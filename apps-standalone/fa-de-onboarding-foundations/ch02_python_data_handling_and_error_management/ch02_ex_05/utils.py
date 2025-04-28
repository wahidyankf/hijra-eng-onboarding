def validate_quantity(quantity, max_quantity):  # Takes quantity and max
    """Validate quantity as integer within limit."""
    cleaned = quantity.strip()  # Clean string
    is_valid = (
        cleaned.isdigit() and int(cleaned) <= max_quantity
    )  # Check format and limit
    print(f"Validating {quantity}: {is_valid}")  # Debug
    return is_valid  # Return result
