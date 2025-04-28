import csv  # For CSV parsing

# Read CSV and check prices
csv_path = "data/sales.csv"  # CSV path
file = open(csv_path, "r")  # Open file
reader = csv.DictReader(file)  # Create DictReader
for row in reader:  # Loop through rows
    price = row["price"].strip()  # Clean price
    print("Price:", price)  # Debug: print price
    if not price.replace(".", "", 1).isdigit():  # Check if numeric
        print("Invalid price:", price)  # Debug: log error
file.close()  # Close file

# Expected Output (abridged):
# Price: 999.99
# Price: invalid
# Invalid price: invalid
# ...
