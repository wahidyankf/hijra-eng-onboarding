# Create a tuple for a transaction
transaction = ("T001", "2023-10-01", "Halal Laptop")  # Tuple for ID, date, product

# Access
print("Transaction ID:", transaction[0])  # Access index 0
print("Transaction Tuple:", transaction)  # Debug: print tuple

# Unpack tuple
trans_id, date, product = transaction  # Unpack into variables
print("Unpacked:", trans_id, date, product)  # Debug: print variables
if product.startswith("Halal"):  # Validate Halal product
    print("Sharia-compliant transaction")  # Confirm compliance

# Expected Output:
# Transaction ID: T001
# Transaction Tuple: ('T001', '2023-10-01', 'Halal Laptop')
# Unpacked: T001 2023-10-01 Halal Laptop
# Sharia-compliant transaction
