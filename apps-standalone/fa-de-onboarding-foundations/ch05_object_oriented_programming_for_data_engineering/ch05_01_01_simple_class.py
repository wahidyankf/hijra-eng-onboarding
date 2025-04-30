# File: de-onboarding/simple_class.py
class Transaction:  # Define Transaction class
    def __init__(self, product, price, quantity):  # Constructor
        self.product = product  # Instance attribute
        self.price = price  # Instance attribute
        self.quantity = quantity  # Instance attribute

    def calculate_amount(self):  # Method to compute amount
        return self.price * self.quantity  # Return price * quantity


# Create objects
sale1 = Transaction("Halal Laptop", 999.99, 2)  # Instantiate object
sale2 = Transaction("Halal Mouse", 24.99, 10)  # Instantiate object

# Access attributes and methods
print(f"Sale 1: {sale1.product}, Amount: ${sale1.calculate_amount()}")  # Debug
print(f"Sale 2: {sale2.product}, Amount: ${sale2.calculate_amount()}")  # Debug

# Expected Output:
# Sale 1: Halal Laptop, Amount: $1999.98
# Sale 2: Halal Mouse, Amount: $249.9
