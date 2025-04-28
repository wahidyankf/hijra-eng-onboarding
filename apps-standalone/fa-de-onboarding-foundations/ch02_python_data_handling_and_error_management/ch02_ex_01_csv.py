import csv  # For CSV parsing


def read_csv(csv_path):  # Takes CSV path
    """Read CSV into list of dictionaries."""
    file = open(csv_path, "r")  # Open file
    reader = csv.DictReader(file)  # Create DictReader
    data = [row for row in reader]  # List comprehension
    file.close()  # Close file
    print("Read data:", data)  # Debug
    return data  # Return list


# Test
print(read_csv("data/sales.csv"))  # Call function

# Output (abridged):
# Read data: [{'product': 'Halal Laptop', 'price': '999.99', 'quantity': '2'}, ...]
# [{'product': 'Halal Laptop', 'price': '999.99', 'quantity': '2'}, ...]
