def validate_sharia_sale(sale):  # Takes sale dictionary
    """Validate sale for Sharia compliance (Halal prefix, sharia_compliant flag)."""
    print("Validating:", sale)  # Debug
    if not sale["product"] or sale["product"].strip() == "":
        return False
    if not sale["product"].startswith("Halal"):
        return False
    if not sale.get("sharia_compliant", False):  # Check flag, default False
        return False
    return True


# Test
print(
    validate_sharia_sale(
        {
            "product": "Halal Laptop",
            "price": "999.99",
            "quantity": "2",
            "sharia_compliant": True,
        }
    )
)

# Output:
# Validating: {'product': 'Halal Laptop', 'price': '999.99', 'quantity': '2', 'sharia_compliant': True}
# True
