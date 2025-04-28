import csv  # For CSV parsing
import json  # For JSON output

# Read CSV file
csv_path = "data/sales.csv"  # Path to sales CSV
file = open(csv_path, "r")  # Open file in read mode
reader = csv.DictReader(file)  # Create DictReader
sales = []  # List to store sales
for row in reader:  # Loop through rows
    sales.append(row)  # Append dictionary
file.close()  # Close file

# Print sales for debugging
print("Sales data:", sales)  # Debug: print sales list

# Write to JSON
json_path = "data/output.json"  # Output path
file = open(json_path, "w")  # Open file in write mode
json.dump(sales, file, indent=2)  # Write JSON with indentation
file.close()  # Close file
print(f"Exported to {json_path}")  # Confirm export

# Expected Output:
# Sales data: [{'product': 'Halal Laptop', 'price': '999.99', 'quantity': '2'}, ...]
# Exported to data/output.json
