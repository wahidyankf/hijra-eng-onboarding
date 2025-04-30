# File: de-onboarding/fetcher.py
class Transaction:  # Define Transaction class
    def __init__(self, product, price, quantity):  # Constructor
        self.product = product  # Instance attribute
        self.price = price  # Instance attribute
        self.quantity = quantity  # Instance attribute

    def calculate_amount(self):  # Method
        return self.price * self.quantity  # Return amount
