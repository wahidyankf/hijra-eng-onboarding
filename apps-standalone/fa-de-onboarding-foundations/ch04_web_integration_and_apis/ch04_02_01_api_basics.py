import requests  # Import requests library

# Fetch transactions from mock API
url = "https://jsonplaceholder.typicode.com/posts"  # Mock API endpoint
response = requests.get(url)  # Send GET request

# Check response status
print("Status Code:", response.status_code)  # Debug: print status
if response.status_code == 200:  # Success
    data = response.json()  # Parse JSON
    print("Data:", data)  # Debug: print data
else:
    print("Failed to fetch data")  # Log failure

# Expected Output (with mock API):
# Status Code: 200
# Data: [{'transaction_id': 'T001', 'product': 'Halal Laptop', 'price': 999.99, 'quantity': 2, 'date': '2023-10-01'}, ...]
