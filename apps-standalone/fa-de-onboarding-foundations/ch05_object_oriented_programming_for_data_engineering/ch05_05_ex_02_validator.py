class Transaction:  # Base class
    def __init__(self, product, price, quantity):  # Constructor
        self.product = product  # Attribute
        self.price = price  # Attribute
        self.quantity = quantity  # Attribute

    def calculate_amount(self):  # Method
        return self.price * self.quantity  # Return amount


class ValidatedTransaction(Transaction):  # Subclass
    def __init__(self, product, price, quantity, prefix):  # Constructor
        super().__init__(product, price, quantity)  # Call base
        self.prefix = prefix  # Attribute

    def is_valid(self):  # Method
        return self.product.startswith(self.prefix)  # Validate


# Test
sale = ValidatedTransaction("Halal Laptop", 999.99, 2, "Halal")  # Instantiate
print(f"Valid: {sale.is_valid()}, Amount: ${sale.calculate_amount()}")  # Print

# Output:
# Valid: True, Amount: $1999.98
