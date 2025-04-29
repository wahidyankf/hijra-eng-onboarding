import csv  # For CSV parsing
import yaml  # For YAML parsing
import json  # For JSON output
import utils  # Import custom utils module


# Define function to read YAML configuration
def read_config(config_path):  # Takes config file path
    """Read YAML configuration."""
    print(f"Opening config: {config_path}")  # Debug: print path
    file = open(config_path, "r")  # Open YAML
    config = yaml.safe_load(file)  # Parse YAML
    file.close()  # Close file
    print(f"Loaded config: {config}")  # Debug: print config
    return config  # Return config dictionary


# Define function to load and validate sales
def load_and_validate_sales(csv_path, config):  # Takes CSV path and config
    """Load sales CSV and validate."""
    print(f"Loading CSV: {csv_path}")  # Debug: print path
    file = open(csv_path, "r")  # Open CSV
    reader = csv.DictReader(file)  # Create DictReader
    valid_sales = []  # List for valid sales
    invalid_count = 0  # Count invalid sales

    # Check for required columns
    required_fields = config["required_fields"]  # Get required fields
    missing_fields = [f for f in required_fields if f not in reader.fieldnames]
    if missing_fields:  # Check for missing columns
        print(f"Invalid CSV: missing columns {missing_fields}")  # Log error
        file.close()  # Close file
        return [], 1  # Return empty list and increment invalid count

    for row in reader:  # Loop through rows
        print(f"Processing row: {row}")  # Debug: print row
        if utils.validate_sale(row, config):  # Validate row
            valid_sales.append(row)  # Append valid sale
        else:
            invalid_count += 1  # Increment invalid count

    file.close()  # Close file
    print(f"Valid sales: {valid_sales}")  # Debug: print valid sales
    return valid_sales, invalid_count  # Return valid sales and invalid count


# Define function to process sales
def process_sales(sales):  # Takes list of sales
    """Process sales: compute total and unique products."""
    if not sales:  # Check for empty sales
        print("No valid sales data")  # Log empty
        return {"total_sales": 0.0, "unique_products": []}, 0

    total_sales = 0.0  # Initialize total
    unique_products = set()  # Set for unique products
    for sale in sales:  # Loop through sales
        price = float(sale["price"])  # Convert price
        quantity = int(sale["quantity"])  # Convert quantity
        amount = price * quantity  # Compute amount
        total_sales += amount  # Add to total
        unique_products.add(sale["product"])  # Add product to set

    results = {
        "total_sales": total_sales,  # Total sales
        "unique_products": list(unique_products),  # Convert set to list
    }
    print(f"Processed results: {results}")  # Debug: print results
    return results, len(sales)  # Return results and valid count


# Define function to export results
def export_results(results, json_path):  # Takes results and file path
    """Export results to JSON."""
    print(f"Writing to: {json_path}")  # Debug: print path
    file = open(json_path, "w")  # Open JSON file
    json.dump(results, file, indent=2)  # Write JSON
    file.close()  # Close file
    print(f"Exported results to {json_path}")  # Confirm export


# Define main function
def main():  # No parameters
    """Main function to process sales data."""
    csv_path = "data/sales.csv"  # CSV path
    config_path = "data/config.yaml"  # YAML path
    json_path = "data/sales_results.json"  # JSON output path

    config = read_config(config_path)  # Read config
    sales, invalid_count = load_and_validate_sales(
        csv_path, config
    )  # Load and validate
    results, valid_count = process_sales(sales)  # Process sales
    export_results(results, json_path)  # Export results

    # Output report
    print("\nSales Report:")  # Print header
    print(f"Total Records Processed: {valid_count + invalid_count}")  # Total records
    print(f"Valid Sales: {valid_count}")  # Valid count
    print(f"Invalid Sales: {invalid_count}")  # Invalid count
    print(f"Total Sales: ${round(results['total_sales'], 2)}")  # Total sales
    print(f"Unique Products: {results['unique_products']}")  # Products
    print("Processing completed")  # Confirm completion


if __name__ == "__main__":
    main()  # Run main function
