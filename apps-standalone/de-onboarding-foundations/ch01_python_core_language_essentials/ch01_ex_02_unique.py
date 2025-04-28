def get_unique_products(sales):  # Takes list of sales
    """Extract unique products using a set."""
    products = set()  # Initialize set
    for sale in sales:  # Iterate over sales
        products.add(sale["product"])  # Add product
    print("Products:", products)  # Debug
    return list(products)  # Return list


# Test
sales = [
    {"product": "Halal Laptop", "price": "999.99", "quantity": "2"},
    {"product": "Halal Mouse", "price": "24.99", "quantity": "10"},
    {"product": "Halal Laptop", "price": "999.99", "quantity": "1"},
]
print(get_unique_products(sales))  # Call function

# Output:
# Products: {'Halal Laptop', 'Halal Mouse'}
# ['Halal Laptop', 'Halal Mouse']
