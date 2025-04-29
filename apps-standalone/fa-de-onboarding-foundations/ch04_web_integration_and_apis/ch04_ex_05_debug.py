import requests  # Import requests


def fetch_data(url):  # Takes URL
    """Fetch JSON data from API."""
    response = requests.get(url)  # Send GET request
    if response.status_code == 200:  # Check success
        data = response.json()  # Parse JSON
        print(f"DEBUG: Fetched {len(data)} records")  # Debug
        return data
    print(f"DEBUG: Fetch failed: {response.status_code}")  # Log failure
    return []  # Return empty list


# Test
print(fetch_data("https://jsonplaceholder.typicode.com/posts"))

# Output:
# DEBUG: Fetched 100 records
# [{'userId': 1, 'id': 1, 'title': '...', 'body': '...'}, ...]
