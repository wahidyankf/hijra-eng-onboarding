# Create a set of products
products = {"Halal Laptop", "Halal Mouse", "Halal Laptop"}  # Set with duplicates

# Add and check
products.add("Halal Keyboard")  # Add new product
print("Products:", products)  # Debug: print set
print("Has Halal Mouse?:", "Halal Mouse" in products)  # Check membership

# Expected Output:
# Products: {'Halal Laptop', 'Halal Mouse', 'Halal Keyboard'}
# Has Halal Mouse?: True
