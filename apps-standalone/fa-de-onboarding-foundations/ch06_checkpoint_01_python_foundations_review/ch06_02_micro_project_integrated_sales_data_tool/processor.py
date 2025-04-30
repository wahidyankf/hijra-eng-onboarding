# File: de-onboarding/processor.py
import pandas as pd
import numpy as np
from utils import is_numeric_value, is_integer, apply_valid_decimals


class SalesProcessor:
    """Class to process sales data."""

    def __init__(self, df, config):  # Initialize with DataFrame and config
        self.df = df  # Store DataFrame
        self.config = config  # Store config
        print("Initialized SalesProcessor")  # Debug

    def validate_data(self):  # Validate DataFrame
        """Validate sales data using config."""
        required_fields = self.config["required_fields"]
        missing_fields = [f for f in required_fields if f not in self.df.columns]
        if missing_fields:
            print(f"Missing columns: {missing_fields}")  # Log error
            return pd.DataFrame()  # Return empty DataFrame

        df = self.df.dropna(subset=["product"])  # Drop missing products
        df = df[
            df["product"].str.startswith(self.config["product_prefix"])
        ]  # Halal filter
        df = df[df["quantity"].apply(is_integer)]  # Integer quantities
        df["quantity"] = df["quantity"].astype(int)  # Convert to int
        df = df[df["quantity"] <= self.config["max_quantity"]]  # Max quantity
        df = df[df["price"].apply(is_numeric_value)]  # Numeric prices
        df = df[df["price"] > 0]  # Positive prices
        df = df[df["price"] >= self.config["min_price"]]  # Min price
        df = df[
            df["price"].apply(
                lambda x: apply_valid_decimals(x, self.config["max_decimals"])
            )
        ]  # Decimals
        print("Validated DataFrame (first 3 rows):")  # Debug
        print(df.head(3))  # Show first 3 rows
        self.df = df  # Update DataFrame

        return df

    def compute_metrics(self):  # Compute sales metrics
        """Compute total sales and top products."""
        if self.df.empty:
            print("No valid data")  # Log empty
            return {"total_sales": 0.0, "unique_products": [], "top_products": {}}

        self.df["amount"] = self.df["price"] * self.df["quantity"]  # Compute amount
        total_sales = np.sum(self.df["amount"].values)  # Total sales
        unique_products = self.df["product"].unique().tolist()  # Unique products
        sales_by_product = self.df.groupby("product")[
            "amount"
        ].sum()  # Group by product
        top_products = (
            sales_by_product.sort_values(ascending=False).head(3).to_dict()
        )  # Top 3
        print("Metrics computed")  # Debug
        return {
            "total_sales": float(total_sales),
            "unique_products": unique_products,
            "top_products": top_products,
        }

    def plot_sales(self, plot_path):  # Generate plot
        """Generate sales plot."""
        import matplotlib.pyplot as plt

        if self.df.empty:
            print("No data to plot")  # Log empty
            return
        plt.figure(figsize=(8, 6))  # Set size
        plt.bar(self.df["product"], self.df["amount"])  # Bar plot
        plt.title("Sales Summary")  # Title
        plt.xlabel("Product")  # X-axis
        plt.ylabel("Sales Amount ($)")  # Y-axis
        plt.xticks(rotation=45)  # Rotate labels
        plt.grid(True)  # Add grid
        plt.tight_layout()  # Adjust layout
        plt.savefig(plot_path, dpi=100)  # Save plot
        plt.close()  # Close figure
        print(f"Plot saved to {plot_path}")  # Confirm
