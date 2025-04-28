# Validate a sale
price = 999.99
quantity = 2
product = "Halal Laptop"

if (
    price > 0 and quantity > 0 and product.startswith("Halal")
):  # Check positive values and compliance
    amount = price * quantity  # Calculate amount
    print("Valid Sharia-compliant Sale, Amount:", amount)  # Output amount
else:
    print("Invalid Sale")  # Output invalid

# Expected Output:
# Valid Sharia-compliant Sale, Amount: 1999.98
