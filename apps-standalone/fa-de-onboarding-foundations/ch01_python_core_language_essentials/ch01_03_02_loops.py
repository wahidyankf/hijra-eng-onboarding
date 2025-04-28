# Sum sales amounts
sales = [1999.98, 249.90, 249.95]
total = 0
for amount in sales:  # Iterate over list
    total += amount  # Accumulate
print("Total Sales:", total)  # Output total

# Count valid sales
count = 0
index = 0
while index < len(sales):  # Loop until end
    if sales[index] > 0:  # Check positive
        count += 1  # Increment count
    index += 1  # Move to next
print("Valid Sales Count:", count)  # Output count

# Expected Output:
# Total Sales: 2499.83
# Valid Sales Count: 3
