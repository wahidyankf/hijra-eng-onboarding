# File: de-onboarding/sales_analyzer.py
# Sales Data Analyzer for processing sales.csv


def is_numeric(s):  # Check if string is a decimal number
    """Check if string is a decimal number."""
    parts = s.split(".")  # Split on decimal point
    if len(parts) != 2 or not parts[0].isdigit() or not parts[1].isdigit():
        return False  # Invalid format
    return True  # Valid decimal


def clean_string(s):  # Clean string by stripping whitespace
    """Strip whitespace from string."""
    return s.strip()


def validate_sale(sale):  # Validate a sale dictionary
    """Validate sale for non-empty product, numeric price/quantity, positive values."""
    print(f"Validating sale: {sale}")  # Debug: print sale
    # Check for missing or empty fields
    if not sale["product"] or sale["product"].strip() == "":
        print(f"Invalid sale: missing product: {sale}")  # Log invalid
        return False

    # Validate price: numeric and positive
    price = clean_string(sale["price"])
    if not is_numeric(price) or float(price) <= 0:
        print(f"Invalid sale: invalid price: {sale}")  # Log invalid
        return False

    # Validate quantity: integer and positive
    quantity = clean_string(sale["quantity"])
    if not quantity.isdigit() or int(quantity) <= 0:
        print(f"Invalid sale: invalid quantity: {sale}")  # Log invalid
        return False

    return True  # Return True if all checks pass


def parse_csv(csv_path):  # Read and parse CSV
    """Read sales CSV and return list of sale dictionaries."""
    sales = []  # List to store sales
    print(f"Opening CSV: {csv_path}")  # Debug: print path
    file = open(csv_path, "r")  # Open file
    lines = file.readlines()  # Read all lines
    file.close()  # Close file

    # Skip header
    for line in lines[1:]:  # Start from second line
        print(f"Parsing line: {line.strip()}")  # Debug: print line
        parts = line.strip().split(",")  # Split on comma
        print(f"Fields: {len(parts)}")  # Debug: print number of fields
        if len(parts) != 3:  # Check for correct number of fields
            print(f"Invalid line format: {line.strip()}")  # Log invalid
            continue
        sale = {
            "product": parts[0],
            "price": parts[1],
            "quantity": parts[2],
        }  # Create sale dictionary
        sales.append(sale)  # Add to list

    print(f"Parsed sales: {sales}")  # Debug: print sales
    return sales  # Return list


def calculate_sales(sales):  # Process sales and compute metrics
    """Calculate total sales and unique products."""
    total_sales = 0.0  # Initialize total
    unique_products = set()  # Set for unique products
    valid_sales = 0  # Count valid sales
    invalid_sales = 0  # Count invalid sales

    for sale in sales:  # Iterate over sales
        if validate_sale(sale):  # Validate sale
            price = float(sale["price"])  # Convert price
            quantity = int(sale["quantity"])  # Convert quantity
            amount = price * quantity  # Calculate amount
            total_sales += amount  # Add to total
            unique_products.add(sale["product"])  # Add product to set
            valid_sales += 1  # Increment valid count
            print(f"Valid sale, amount: {amount}")  # Debug: print amount
        else:
            invalid_sales += 1  # Increment invalid count

    return {
        "total_sales": total_sales,
        "unique_products": list(unique_products),
        "valid_sales": valid_sales,
        "invalid_sales": invalid_sales,
    }  # Return results


def main():  # Main function
    """Main function to analyze sales data."""
    csv_path = "data/sales.csv"  # CSV path
    sales = parse_csv(csv_path)  # Parse CSV
    results = calculate_sales(sales)  # Calculate metrics

    # Output report
    print("\nSales Report:")  # Print header
    print(f"Total Sales: ${round(results['total_sales'], 2)}")  # Total sales
    print(f"Unique Products: {results['unique_products']}")  # Products
    print(f"Valid Sales: {results['valid_sales']}")  # Valid count
    print(f"Invalid Sales: {results['invalid_sales']}")  # Invalid count
    print("Processing completed")  # Confirm completion


if __name__ == "__main__":
    main()  # Run main function
