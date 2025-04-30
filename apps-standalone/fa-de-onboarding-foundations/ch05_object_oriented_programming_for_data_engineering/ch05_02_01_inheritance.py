# File: de-onboarding/inheritance.py
class BaseTransaction:  # Base class
    def __init__(self, product, price, quantity):  # Constructor
        self.product = product  # Attribute
        self.price = price  # Attribute
        self.quantity = quantity  # Attribute

    def calculate_amount(self):  # Method
        return self.price * self.quantity  # Return amount


class ValidatedTransaction(BaseTransaction):  # Subclass
    def __init__(self, product, price, quantity, prefix):  # Constructor
        super().__init__(product, price, quantity)  # Call base constructor
        self.prefix = prefix  # Additional attribute

    def is_valid(self):  # New method
        return (
            self.product.startswith(self.prefix)
            and self.price > 0
            and self.quantity > 0
        )


# Create objects
sale = ValidatedTransaction("Halal Laptop", 999.99, 2, "Halal")  # Instantiate
print(f"Valid: {sale.is_valid()}, Amount: ${sale.calculate_amount()}")  # Debug

# Expected Output:
# Valid: True, Amount: $1999.98
