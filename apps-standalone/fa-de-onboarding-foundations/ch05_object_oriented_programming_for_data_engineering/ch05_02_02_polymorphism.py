# File: de-onboarding/polymorphism.py
class BaseTransaction:  # Base class
    def __init__(self, product, price, quantity):  # Constructor
        self.product = product  # Attribute
        self.price = price  # Attribute
        self.quantity = quantity  # Attribute

    def calculate_amount(self):  # Method
        return self.price * self.quantity  # Base implementation


class DiscountedTransaction(BaseTransaction):  # Subclass
    def __init__(self, product, price, quantity, discount):  # Constructor
        super().__init__(product, price, quantity)  # Call base
        self.discount = discount  # Additional attribute

    def calculate_amount(self):  # Override method
        base_amount = super().calculate_amount()  # Call base method
        return base_amount * (1 - self.discount)  # Apply discount


# Create objects
sale = DiscountedTransaction("Halal Laptop", 999.99, 2, 0.1)  # 10% discount
print(f"Discounted Amount: ${sale.calculate_amount()}")  # Debug

# Expected Output:
# Discounted Amount: $1799.982
