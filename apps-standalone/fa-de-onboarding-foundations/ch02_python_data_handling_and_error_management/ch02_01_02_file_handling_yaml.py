import yaml  # For YAML parsing

# Read YAML file
config_path = "data/config.yaml"  # Path to config
file = open(config_path, "r")  # Open file
config = yaml.safe_load(file)  # Parse YAML
file.close()  # Close file

# Print config for debugging
print("Config:", config)  # Debug: print config

# Expected Output:
# Config: {'min_price': 10.0, 'max_quantity': 100, 'required_fields': ['product', 'price', 'quantity'], 'product_prefix': 'Halal', 'max_decimals': 2}
