# File: de-onboarding/solid.py
class DataFetcher:  # Single responsibility: fetch data
    def fetch_data(self, source):  # Method
        print(f"Fetching from {source}")  # Debug
        return [{"product": "Halal Laptop", "price": 999.99, "quantity": 2}]


class ValidatedDataFetcher(DataFetcher):  # Liskov Substitution: extends fetcher
    def fetch_data(self, source):  # Override method
        data = super().fetch_data(source)  # Call base
        if all(item["product"].startswith("Halal") for item in data):  # Validate
            print("Validated data")  # Debug
            return data
        return []  # Return empty if invalid


class DataValidator:  # Single responsibility: validate data
    def validate(self, data, prefix):  # Method
        return all(item["product"].startswith(prefix) for item in data)


class Pipeline(DataFetcher):  # Open for extension
    def process(self, source, prefix):  # Method
        data = self.fetch_data(source)  # Fetch
        validator = DataValidator()  # Create validator
        if validator.validate(data, prefix):  # Validate
            print("Data valid")  # Debug
            return data
        print("Data invalid")  # Debug
        return []


# Create objects
pipeline = Pipeline()  # Instantiate Pipeline
result = pipeline.process("csv", "Halal")  # Call method
print(f"Pipeline Result: {result}")  # Debug

validated_fetcher = ValidatedDataFetcher()  # Instantiate ValidatedDataFetcher
result = validated_fetcher.fetch_data("csv")  # Call method (Liskov Substitution)
print(f"Validated Fetcher Result: {result}")  # Debug

# Expected Output:
# Fetching from csv
# Data valid
# Pipeline Result: [{'product': 'Halal Laptop', 'price': 999.99, 'quantity': 2}]
# Fetching from csv
# Validated data
# Validated Fetcher Result: [{'product': 'Halal Laptop', 'price': 999.99, 'quantity': 2}]
