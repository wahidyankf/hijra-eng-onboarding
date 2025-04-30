# File: fetcher.py
import pandas as pd  # For DataFrame operations
import yaml  # For YAML parsing
import utils  # Import utils module


class ConfigReader:  # Single responsibility: read config
    def __init__(self, config_path):  # Constructor
        self.config_path = config_path  # Store path
        self.config = self.read_config()  # Load config

    def read_config(self):  # Read YAML
        print(f"Opening config: {self.config_path}")  # Debug
        file = open(self.config_path, "r")  # Open file
        config = yaml.safe_load(file)  # Parse YAML
        file.close()  # Close file
        print(f"Loaded config: {config}")  # Debug
        return config  # Return config


class TransactionFetcher:  # Single responsibility: fetch data
    def fetch_data(self, csv_path):  # Simulate API fetch with CSV
        print(f"Fetching data from: {csv_path}")  # Debug
        df = pd.read_csv(csv_path)  # Load CSV
        print("Fetched DataFrame:")  # Debug
        print(df.head())  # Show first rows
        return df  # Return DataFrame


class TransactionValidator:  # Single responsibility: validate data
    def __init__(self, config):  # Constructor
        self.config = config  # Store config

    def validate_data(self, df):  # Validate DataFrame
        print("Validating data...")  # Debug
        required_fields = self.config["required_fields"]  # Get fields
        missing_fields = [f for f in required_fields if f not in df.columns]
        if missing_fields:  # Check columns
            print(f"Missing columns: {missing_fields}")  # Log
            return pd.DataFrame()  # Return empty

        # Filter valid records
        df = df.dropna(subset=["product"])  # Drop missing product
        df = df[
            df["product"].str.startswith(self.config["product_prefix"])
        ]  # Filter Halal
        df = df[df["quantity"].apply(utils.is_integer)]  # Ensure integer quantity
        df["quantity"] = df["quantity"].astype(int)  # Convert to int
        df = df[df["quantity"] <= self.config["max_quantity"]]  # Filter quantity
        df = df[df["quantity"] > 0]  # Filter positive quantity
        df = df[df["price"].apply(utils.is_numeric_value)]  # Ensure numeric price
        df = df[df["price"] > 0]  # Filter positive price
        df = df[df["price"] >= self.config["min_price"]]  # Filter min price
        df = df[
            df["price"].apply(
                lambda x: utils.apply_valid_decimals(x, self.config["max_decimals"])
            )
        ]  # Check decimals

        print("Validated DataFrame:")  # Debug
        print(df)  # Show filtered
        return df  # Return validated


class TransactionProcessor(TransactionFetcher):  # Inherits fetcher
    def __init__(self, config):  # Constructor
        self.config = config  # Store config
        self.validator = TransactionValidator(config)  # Create validator

    def process_data(self, csv_path):  # Process data
        df = self.fetch_data(csv_path)  # Fetch data
        df = self.validator.validate_data(df)  # Validate
        if df.empty:  # Check empty
            print("No valid data")  # Log
            return {"total_sales": 0.0, "unique_products": [], "top_products": {}}, 0

        # Compute metrics
        df["amount"] = df["price"] * df["quantity"]  # Compute amount
        total_sales = df["amount"].sum()  # Total sales
        unique_products = df["product"].unique().tolist()  # Unique products
        sales_by_product = df.groupby("product")["amount"].sum()  # Group
        top_products = (
            sales_by_product.sort_values(ascending=False).head(3).to_dict()  # type: ignore
        )  # Top 3

        valid_sales = len(df)  # Count valid
        print(f"Valid sales: {valid_sales} records")  # Debug
        return {
            "total_sales": float(total_sales),  # Convert for JSON
            "unique_products": unique_products,  # Products
            "top_products": top_products,  # Top products
        }, valid_sales  # Return results
