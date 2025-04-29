import pandas as pd  # Import Pandas
import matplotlib.pyplot as plt  # Import Matplotlib


def plot_sales(csv_path, plot_path):  # Takes CSV and plot paths
    """Plot sales by product."""
    df = pd.read_csv(csv_path)  # Load CSV
    df["amount"] = df["price"] * df["quantity"]  # Compute amount
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


# Test
plot_sales("data/sample.csv", "data/plot.png")  # Call function

# Output:
# Plot saved to data/plot.png
