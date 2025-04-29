import pandas as pd  # For DataFrame operations
import numpy as np  # For numerical computations
import yaml  # For YAML parsing
import json  # For JSON export
import matplotlib.pyplot as plt  # For plotting
import utils  # Import custom utils module
import os  # For file existence check


# Define function to read YAML configuration
def read_config(config_path):  # Takes config file path
    """Read YAML configuration."""
    print(f"Opening config: {config_path}")  # Debug: print path
    file = open(config_path, "r")  # Open YAML
    config = yaml.safe_load(file)  # Parse YAML
    file.close()  # Close file
    print(f"Loaded config: {config}")  # Debug: print config
    return config  # Return config dictionary


# Define function to load and validate sales data
def load_and_validate_sales(csv_path, config):  # Takes CSV path and config
    """Load sales CSV and validate using Pandas."""
    print(f"Loading CSV: {csv_path}")  # Debug: print path
    # Load CSV and coerce price to numeric, invalids become NaN
    df = pd.read_csv(csv_path)
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    print("Initial DataFrame:")
    print(df)

    # Check for missing required columns
    missing_fields = [f for f in config["required_fields"] if f not in df.columns]
    if missing_fields:
        print(f"Missing columns: {missing_fields}")
        return pd.DataFrame(), 0, 0

    # Drop rows with missing required fields (including NaN price)
    df = df.dropna(subset=config["required_fields"])

    # Early return if DataFrame is empty after dropping required fields
    if df.empty:
        print("No data available after dropping missing required fields.")
        return df, 0, 0

    df = df[df["quantity"].apply(utils.is_integer)]  # Ensure quantity is integer
    df["quantity"] = df["quantity"].astype(int)
    df = df[df["quantity"] <= config["max_quantity"]]
    df = df[df["price"] > 0]
    df = df[df["price"] >= config["min_price"]]
    total_records = len(df)
    print("Validated DataFrame:")
    print(df)
    return df, len(df), total_records


# Define function to process sales data
def process_sales(df):  # Takes DataFrame
    """Process sales: compute total and top products using Pandas/NumPy."""
    if df.empty:  # Check for empty DataFrame
        print("No valid sales data")  # Log empty
        return {"total_sales": 0.0, "unique_products": [], "top_products": {}}, 0

    # Compute amount
    df["amount"] = (df["price"] * df["quantity"]).round(2)  # Price * quantity, rounded
    print("DataFrame with Amount:")  # Debug
    print(df)  # Show DataFrame with amount

    # Compute metrics using NumPy
    total_sales = float(np.sum(df["amount"].values))  # Total sales
    unique_products = df["product"].unique().tolist()  # Unique products
    sales_by_product = df.groupby("product")["amount"].sum().round(2)
    # Use OrderedDict to preserve order
    from collections import OrderedDict

    top_products = OrderedDict(
        sales_by_product.sort_values(ascending=False).head(3).items()
    )

    valid_sales = len(df)  # Count valid sales
    print(f"Valid sales: {valid_sales} records")  # Log valid count

    return {
        "total_sales": round(total_sales, 2),  # Convert to float for JSON
        "unique_products": unique_products,  # List of products
        "top_products": dict(top_products),  # Top 3 products, ordered
    }, valid_sales  # Return results and count


# Define function to export results
def export_results(results, json_path):  # Takes results and file path
    """Export results to JSON."""
    print(f"Writing to: {json_path}")  # Debug: print path
    print(f"Results: {results}")  # Debug: print results
    file = open(json_path, "w")  # Open JSON file
    json.dump(results, file, indent=2)  # Write JSON
    file.close()  # Close file
    print(f"Exported results to {json_path}")  # Confirm export


# Define function to plot sales
def plot_sales(df, plot_path):  # Takes DataFrame and plot path
    """Generate sales trend plot."""
    if df.empty:  # Check for empty DataFrame
        print("No data to plot")  # Log empty
        return

    plt.figure(figsize=(8, 6))  # Set figure size
    plt.bar(df["product"], df["amount"])  # Bar plot
    plt.title("Sales by Product")  # Title
    plt.xlabel("Product")  # X-axis label
    plt.ylabel("Sales Amount ($)")  # Y-axis label
    plt.xticks(rotation=45)  # Rotate x labels
    plt.grid(True)  # Add grid
    plt.tight_layout()  # Adjust layout
    plt.savefig(plot_path, dpi=100)  # Save plot with high resolution
    plt.close()  # Close figure
    print(f"Plot saved to {plot_path}")  # Confirm save
    print(f"File exists: {os.path.exists(plot_path)}")  # Confirm file creation


# Define main function
def main():  # No parameters
    """Main function to process sales data."""
    csv_path = "data/negative.csv"  # CSV path
    config_path = "data/config.yaml"  # YAML path
    json_path = "data/sales_results.json"  # JSON output path
    plot_path = "data/sales_trend.png"  # Plot output path

    config = read_config(config_path)  # Read config
    df, valid_sales, total_records = load_and_validate_sales(
        csv_path, config
    )  # Load and validate
    results, valid_sales = process_sales(df)  # Process
    export_results(results, json_path)  # Export results
    plot_sales(df, plot_path)  # Generate plot

    # Output report
    print("\nSales Report:")  # Print header
    print(f"Total Records Processed: {total_records}")  # Total records
    print(f"Valid Sales: {valid_sales}")  # Valid count
    print(f"Invalid Sales: {total_records - valid_sales}")  # Invalid count
    print(f"Total Sales: ${round(results['total_sales'], 2)}")  # Total sales
    print(f"Unique Products: {results['unique_products']}")  # Products
    print(f"Top Products: {results['top_products']}")  # Top products
    print("Processing completed")  # Confirm completion


if __name__ == "__main__":
    main()  # Run main function
