# File: de-onboarding/main.py
import fetcher  # Import module

# Create and use objects
sale = fetcher.Transaction("Halal Laptop", 999.99, 2)  # Instantiate
print(f"Product: {sale.product}, Amount: ${sale.calculate_amount()}")  # Debug

# Expected Output:
# Product: Halal Laptop, Amount: $1999.98
