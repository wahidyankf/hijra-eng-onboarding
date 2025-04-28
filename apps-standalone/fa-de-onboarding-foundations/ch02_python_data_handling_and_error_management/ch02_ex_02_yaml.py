import yaml  # For YAML parsing


def parse_yaml(config_path):  # Takes config path
    """Parse YAML file."""
    file = open(config_path, "r")  # Open file
    config = yaml.safe_load(file)  # Parse YAML
    file.close()  # Close file
    print("Parsed config:", config)  # Debug
    return config  # Return dictionary


# Test
print(parse_yaml("data/config.yaml"))  # Call function

# Output:
# Parsed config: {'min_price': 10.0, 'max_quantity': 100, ...}
# {'min_price': 10.0, 'max_quantity': 100, ...}
