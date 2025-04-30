# File: de-onboarding/main.py
import pandas as pd
import yaml
import json
from processor import SalesProcessor


def load_config(config_path):  # Load YAML
    """Load YAML configuration."""
    print(f"Loading config: {config_path}")  # Debug
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    print(f"Config: {config}")  # Debug
    return config


def load_data(csv_path, json_path):  # Load CSV and JSON
    """Load sales CSV and mock API data."""
    print(f"Loading CSV: {csv_path}")  # Debug
    df_csv = pd.read_csv(csv_path)  # Load CSV
    print(f"Loading JSON: {json_path}")  # Debug
    with open(json_path, "r") as f:
        api_data = json.load(f)  # Load JSON
    df_api = pd.DataFrame(api_data)  # Convert to DataFrame
    df = pd.concat([df_csv, df_api], ignore_index=True)  # Combine
    print("Combined DataFrame (first 3 rows):")  # Debug
    print(df.head(3))  # Show first 3 rows
    return df


def export_results(results, json_path):  # Export JSON
    """Export results to JSON."""
    print(f"Writing to: {json_path}")  # Debug
    with open(json_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Exported to {json_path}")  # Confirm


def main():  # Main function
    """Integrate sales data processing."""
    csv_path = "data/sales.csv"
    config_path = "data/config.yaml"
    json_path = "data/mock_api.json"
    output_json = "data/sales_summary.json"
    plot_path = "data/sales_summary.png"

    config = load_config(config_path)  # Load config
    df = load_data(csv_path, json_path)  # Load data
    processor = SalesProcessor(df, config)  # Initialize processor
    _ = processor.validate_data()  # Validate
    results = processor.compute_metrics()  # Compute metrics
    processor.plot_sales(plot_path)  # Plot
    export_results(results, output_json)  # Export

    # Print report
    print("\nSales Report:")
    print(f"Total Sales: ${round(results['total_sales'], 2)}")
    print(f"Unique Products: {results['unique_products']}")
    print(f"Top Products: {results['top_products']}")
    print("Processing completed")


if __name__ == "__main__":
    main()
