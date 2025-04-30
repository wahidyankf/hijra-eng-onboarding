# File: de-onboarding/main.py
import fetcher  # Import module
import json  # For JSON export
import os  # For file checks


def export_results(results, json_path):  # Export results
    """Export results to JSON."""
    print(f"Writing to: {json_path}")  # Debug
    print(f"Results: {results}")  # Debug
    file = open(json_path, "w")  # Open file
    json.dump(results, file, indent=2)  # Write JSON
    file.close()  # Close file
    print(f"Exported to {json_path}")  # Confirm


def main():  # Main function
    csv_path = "data/transactions.csv"  # CSV path
    config_path = "data/config.yaml"  # Config path
    json_path = "data/transactions_results.json"  # JSON path

    config_reader = fetcher.ConfigReader(config_path)  # Create reader
    config = config_reader.config  # Get config
    processor = fetcher.TransactionProcessor(config)  # Create processor
    results, valid_sales = processor.process_data(csv_path)  # Process
    total_records = valid_sales  # Total after filtering
    export_results(results, json_path)  # Export

    # Print report
    print("\nTransaction Report:")  # Header
    print(f"Total Records Processed: {total_records}")  # Total
    print(f"Valid Sales: {valid_sales}")  # Valid
    print(f"Invalid Sales: {total_records - valid_sales}")  # Invalid
    print(f"Total Sales: ${round(results['total_sales'], 2)}")  # Total sales
    print(f"Unique Products: {results['unique_products']}")  # Products
    print(f"Top Products: {results['top_products']}")  # Top products
    print("Processing completed")  # Confirm


if __name__ == "__main__":
    main()  # Run main
