# Create a sale dictionary
sale = {
    "product": "Halal Laptop",
    "price": 999.99,
    "quantity": 2,
    "sharia_compliant": True,
}  # Dictionary for one sale

# Access and modify
print("Product:", sale["product"])  # Access by key
if sale["sharia_compliant"] and sale["product"].startswith(
    "Halal"
):  # Validate compliance
    sale["amount"] = sale["price"] * sale["quantity"]  # Add amount
print("Sale:", sale)  # Debug: print dictionary

# Iterate over keys/values
for key, value in sale.items():  # Loop through key-value pairs
    print(f"{key}: {value}")  # Print each pair

# Expected Output:
# Product: Halal Laptop
# Sale: {'product': 'Halal Laptop', 'price': 999.99, 'quantity': 2, 'sharia_compliant': True, 'amount': 1999.98}
# product: Halal Laptop
# price: 999.99
# quantity: 2
# sharia_compliant: True
# amount: 1999.98
