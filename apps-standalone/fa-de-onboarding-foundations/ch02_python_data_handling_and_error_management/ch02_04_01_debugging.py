import csv  # For CSV parsing

# Read and validate CSV
csv_path = "data/sales.csv"  # CSV path
file = open(csv_path, "r")  # Open file
reader = csv.DictReader(file)  # Create DictReader
for row in reader:  # Loop through rows
    print("Processing row:", row)  # Debug: print row
    product = row["product"].strip()  # Clean product
    print("Cleaned product:", product)  # Debug: print cleaned
    if not product:  # Check for empty product
        print("Invalid: Missing product")  # Debug: log error
file.close()  # Close file
