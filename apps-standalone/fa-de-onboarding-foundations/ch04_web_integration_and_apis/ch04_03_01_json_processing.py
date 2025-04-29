import requests  # Import requests

# Fetch and process JSON
url = "https://jsonplaceholder.typicode.com/posts"  # Mock API
response = requests.get(url)  # Send GET request
if response.status_code == 200:  # Check success
    transactions = response.json()  # Parse JSON
    print("Response JSON:", transactions)  # Debug: print raw JSON
    for transaction in transactions:  # Loop through transactions
        print(f"Processing: {transaction}")  # Debug: print transaction
        # Example: Access fields
        tid = transaction["id"]  # Get ID
        product = transaction["title"]  # Get product
        print(f"ID: {tid}, Product: {product}")  # Debug: print fields
else:
    print("Fetch failed:", response.status_code)  # Log failure

# Expected Output:
# Response JSON: [{'id': 1, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}
# Processing: {'id': 1, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}
# ID: 1, Product: sunt aut facere repellat provident occaecati excepturi optio reprehenderit
# ...
