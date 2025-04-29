import requests  # Import requests

# Fetch and process JSON
url = "https://jsonplaceholder.typicode.com/posts"  # API endpoint
response = requests.get(url)  # Send GET request
if response.status_code == 200:  # Check success
    posts = response.json()  # Parse JSON
    print("DEBUG: Response JSON:", posts[:2])  # Debug: print first two records
    for post in posts:  # Loop through posts
        print(f"DEBUG: Processing post: {post}")  # Debug: print post
        # Example: Access fields
        post_id = post["id"]  # Get ID
        title = post["title"]  # Get title
        print(f"DEBUG: ID: {post_id}, Title: {title}")  # Debug: print fields
else:
    print("DEBUG: Fetch failed:", response.status_code)  # Log failure

# Expected Output:
# DEBUG: Response JSON: [{'userId': 1, 'id': 1, 'title': 'sunt aut facere...', 'body': '...'}, ...]
# DEBUG: Processing post: {'userId': 1, 'id': 1, 'title': 'sunt aut facere...', 'body': '...'}
# DEBUG: ID: 1, Title: sunt aut facere...
# ...
