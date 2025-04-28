# Create a list of sales amounts
sales = [1999.98, 249.90, 249.95]  # List of sale amounts for Halal products

# Access and modify
print("First Sale:", sales[0])  # Access index 0
sales.append(29.97)  # Add new sale
print("Updated Sales:", sales)  # Debug: print list

# Iterate over list
total = 0
for sale in sales:  # Loop through sales
    total += sale  # Accumulate total
print("Total Sales:", total)  # Output total

# Expected Output:
# First Sale: 1999.98
# Updated Sales: [1999.98, 249.9, 249.95, 29.97]
# Total Sales: 2529.8
