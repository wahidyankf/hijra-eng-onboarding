import csv  # For CSV parsing

# Read CSV and check headers
csv_path = "data/sales.csv"  # CSV path
file = open(csv_path, "r")  # Open file
reader = csv.DictReader(file)  # Create DictReader
print("CSV Columns:", reader.fieldnames)  # Debug: print column names
for row in reader:  # Loop through rows
    print("Processing row:", row)  # Debug: print row
file.close()  # Close file

# Expected Output:
# CSV Columns: ['product', 'price', 'quantity']
# Processing row: {'product': 'Halal Laptop', 'price': '999.99', 'quantity': '2'}
# ...
