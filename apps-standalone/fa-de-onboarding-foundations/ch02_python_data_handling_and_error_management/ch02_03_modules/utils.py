def clean_string(s):  # Clean string
    """Strip whitespace from string."""
    return s.strip()  # Return cleaned string


def is_numeric(s, max_decimals=2):  # Check if string is numeric
    """Check if string is a decimal number with up to max_decimals."""
    parts = s.split(".")  # Split on decimal
    if len(parts) != 2 or not parts[0].isdigit() or not parts[1].isdigit():
        return False  # Invalid format
    return len(parts[1]) <= max_decimals  # Check decimal places
