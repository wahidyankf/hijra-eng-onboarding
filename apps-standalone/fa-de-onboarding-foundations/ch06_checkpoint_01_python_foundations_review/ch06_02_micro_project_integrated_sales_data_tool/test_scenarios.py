from main import load_config, load_data, SalesProcessor

config = load_config("data/config.yaml")
test_files = ["empty.csv", "invalid.csv", "malformed.csv", "negative.csv"]
for csv_file in test_files:
    print(f"\nTesting {csv_file}")
    df = load_data(f"data/{csv_file}", "data/mock_api.json")
    processor = SalesProcessor(df, config)
    df_valid = processor.validate_data()
    results = processor.compute_metrics()
    print(f"Results: {results}")
