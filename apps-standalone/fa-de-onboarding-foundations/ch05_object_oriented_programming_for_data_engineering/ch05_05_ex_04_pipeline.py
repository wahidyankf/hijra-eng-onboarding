class BaseFetcher:  # Base class
    def fetch_data(self, source):  # Method
        print(f"Fetching from {source}")  # Debug
        return [{"product": "Halal Laptop", "price": 999.99, "quantity": 2}]


class DataValidator:  # Validator class
    def validate(self, data, prefix):  # Method
        return all(item["product"].startswith(prefix) for item in data)


class DataPipeline(BaseFetcher):  # Pipeline class
    def process(self, source, prefix):  # Method
        data = self.fetch_data(source)  # Fetch
        validator = DataValidator()  # Create validator
        if validator.validate(data, prefix):  # Validate
            print("Data valid")  # Debug
            return data
        print("Data invalid")  # Debug
        return []  # Return empty


# Test
pipeline = DataPipeline()  # Instantiate
result = pipeline.process("csv", "Halal")  # Call
print(f"Result: {result}")  # Print

# Output:
# Fetching from csv
# Data valid
# Result: [{'product': 'Halal Laptop', 'price': 999.99, 'quantity': 2}]
