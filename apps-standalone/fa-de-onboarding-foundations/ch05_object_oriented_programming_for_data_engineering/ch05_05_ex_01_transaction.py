class Transaction:  # Define class
    def __init__(self, product, price, quantity):  # Constructor
        self.product = product  # Attribute
        self.price = price  # Attribute
        self.quantity = quantity  # Attribute

    def calculate_amount(self):  # Method
        return self.price * self.quantity  # Return amount


# Test
sale = Transaction("Halal Laptop", 999.99, 2)  # Instantiate
print(f"Product: {sale.product}, Amount: ${sale.calculate_amount()}")  # Print

# Output:
# Product: Halal Laptop, Amount: $1999.98
