# File: de-onboarding/solid_di.py
import pandas as pd  # For DataFrame operations
import yaml  # For YAML parsing
import json  # For JSON output


class AbstractFetcher:  # Abstraction for Dependency Inversion
    def fetch_data(self, source):  # Abstract method
        pass  # No implementation


class TransactionFetcher(AbstractFetcher):  # Concrete implementation
    def fetch_data(self, source):  # Method
        print(f"Fetching transactions from {source}")  # Debug
        df = pd.read_csv(source)  # Load CSV
        data = df[["product", "price", "quantity"]].to_dict(
            orient="records"
        )  # Convert to list of dicts
        return data  # Return transaction data


class TransactionValidator:  # Single responsibility: validate data
    def __init__(self, config_path):  # Constructor
        with open(config_path, "r") as file:  # Open config
            self.config = yaml.safe_load(file)  # Load YAML
        print(f"Loaded config for validation: {self.config}")  # Debug

    def validate(self, data):  # Validate data
        prefix = self.config["product_prefix"]  # Get prefix
        return [
            item
            for item in data
            if item["product"] and item["product"].startswith(prefix)
        ]  # Filter valid


class TransactionProcessor:  # Depends on abstraction
    def __init__(self, fetcher, validator):  # Constructor
        self.fetcher = fetcher  # Store fetcher (abstract)
        self.validator = validator  # Store validator

    def process(self, source):  # Method
        data = self.fetcher.fetch_data(source)  # Fetch data
        valid_data = self.validator.validate(data)  # Validate
        total_sales = sum(
            item["price"] * item["quantity"] for item in valid_data
        )  # Compute total
        result = {
            "total_sales": total_sales,
            "valid_records": len(valid_data),
        }  # Create result
        print(f"Processed data: {result}")  # Debug
        return result  # Return result


# Create objects
fetcher = TransactionFetcher()  # Instantiate fetcher
validator = TransactionValidator("data/config.yaml")  # Instantiate validator
processor = TransactionProcessor(fetcher, validator)  # Pass fetcher and validator
result = processor.process("data/transactions.csv")  # Call method
with open("data/processor_result.json", "w") as file:  # Save result
    json.dump(result, file, indent=2)  # Write JSON
print(f"Result: {result}")  # Debug

# Expected Output:
# Loaded config for validation: {'min_price': 10.0, 'max_quantity': 100, 'required_fields': ['product', 'price', 'quantity'], 'product_prefix': 'Halal', 'max_decimals': 2}
# Fetching transactions from data/transactions.csv
# Processed data: {'total_sales': 2499.83, 'valid_records': 3}
# Result: {'total_sales': 2499.83, 'valid_records': 3}
# (Creates data/processor_result.json with same result)
