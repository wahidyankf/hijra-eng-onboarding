import pandas as pd  # Import Pandas
import matplotlib.pyplot as plt  # Import Matplotlib

# Load and clean DataFrame
df = pd.read_csv("data/sales.csv")  # Read CSV
df = df.dropna(subset=["product", "price"])  # Drop missing values
df = df[df["product"].str.startswith("Halal")]  # Filter Halal products

# Compute amount
df["amount"] = df["price"] * df["quantity"]  # Price * quantity

# Plot sales by product
plt.figure(figsize=(8, 6))  # Set figure size
plt.bar(df["product"], df["amount"])  # Bar plot
plt.title("Sales by Product")  # Title
plt.xlabel("Product")  # X-axis label
plt.ylabel("Sales Amount ($)")  # Y-axis label
plt.xticks(rotation=45)  # Rotate x labels
plt.grid(True)  # Add grid
plt.tight_layout()  # Adjust layout
plt.savefig("data/sales_plot.png", dpi=100)  # Save plot with high resolution
plt.close()  # Close figure

print("Plot saved to data/sales_plot.png")  # Confirm save

# Expected Output:
# Plot saved to data/sales_plot.png
# (Creates data/sales_plot.png with bar plot)
