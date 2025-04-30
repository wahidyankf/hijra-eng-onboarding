class Transaction:  # Base class
    def __init__(self, product, price, quantity):  # Constructor
        self.product = product  # Attribute
        self.price = price  # Attribute
        self.quantity = quantity  # Attribute


class ValidatedTransaction(Transaction):  # Subclass
    def __init__(self, product, price, quantity, prefix):  # Constructor
        super().__init__(product, price, quantity)  # Fix: Call base
        self.prefix = prefix  # Attribute

    def is_valid(self):  # Method
        return self.product.startswith(self.prefix)  # Validate


# Test
sale = ValidatedTransaction("Halal Laptop", 999.99, 2, "Halal")  # Instantiate
print(sale.is_valid())  # Print

# Output:
# True
