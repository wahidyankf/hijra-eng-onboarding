class Transaction:  # Base class
    def __init__(self, product, price, quantity):  # Constructor
        self.product = product  # Attribute
        self.price = price  # Attribute
        self.quantity = quantity  # Attribute

    def calculate_amount(self):  # Method
        return self.price * self.quantity  # Return amount


class DiscountedTransaction(Transaction):  # Subclass
    def __init__(self, product, price, quantity, discount):  # Constructor
        super().__init__(product, price, quantity)  # Call base
        self.discount = discount  # Attribute

    def calculate_amount(self):  # Override method
        base_amount = super().calculate_amount()  # Call base
        return base_amount * (1 - self.discount)  # Apply discount


# Test
sale = DiscountedTransaction("Halal Laptop", 999.99, 2, 0.1)  # Instantiate
print(f"Discounted Amount: ${sale.calculate_amount()}")  # Print

# Output:
# Discounted Amount: $1799.982
