import requests  # Import requests library

# Base URL
base_url = "https://jsonplaceholder.typicode.com"

# GET: Fetch all posts
response_get = requests.get(f"{base_url}/posts")
print("DEBUG: GET Status Code:", response_get.status_code)
if response_get.status_code == 200:
    print("DEBUG: GET Data:", response_get.json()[:2])

# GET: Fetch single post
response_get_single = requests.get(f"{base_url}/posts/1")
print("DEBUG: GET Single Status Code:", response_get_single.status_code)
if response_get_single.status_code == 200:
    print("DEBUG: GET Single Data:", response_get_single.json())

# GET: Fetch comments for a post
response_get_comments = requests.get(f"{base_url}/comments?postId=1")
print("DEBUG: GET Comments Status Code:", response_get_comments.status_code)
if response_get_comments.status_code == 200:
    print("DEBUG: GET Comments Data:", response_get_comments.json()[:1])

# POST: Create a new post
new_post = {"userId": 1, "title": "new post", "body": "content"}
response_post = requests.post(f"{base_url}/posts", json=new_post)
print("DEBUG: POST Status Code:", response_post.status_code)
if response_post.status_code == 201:
    print("DEBUG: POST Data:", response_post.json())

# PUT: Update a post
updated_post = {"userId": 1, "id": 1, "title": "updated post", "body": "new content"}
response_put = requests.put(f"{base_url}/posts/1", json=updated_post)
print("DEBUG: PUT Status Code:", response_put.status_code)
if response_put.status_code == 200:
    print("DEBUG: PUT Data:", response_put.json())

# PATCH: Partially update a post
partial_update = {"title": "partially updated post"}
response_patch = requests.patch(f"{base_url}/posts/1", json=partial_update)
print("DEBUG: PATCH Status Code:", response_patch.status_code)
if response_patch.status_code == 200:
    print("DEBUG: PATCH Data:", response_patch.json())

# DELETE: Delete a post
response_delete = requests.delete(f"{base_url}/posts/1")
print("DEBUG: DELETE Status Code:", response_delete.status_code)
if response_delete.status_code == 200:
    print("DEBUG: DELETE Data:", response_delete.json())

# Expected Output (abridged):
# DEBUG: GET Status Code: 200
# DEBUG: GET Data: [{'userId': 1, 'id': 1, 'title': 'sunt aut facere...', 'body': '...'}, ...]
# DEBUG: GET Single Status Code: 200
# DEBUG: GET Single Data: {'userId': 1, 'id': 1, 'title': 'sunt aut facere...', 'body': '...'}
# DEBUG: GET Comments Status Code: 200
# DEBUG: GET Comments Data: [{'postId': 1, 'id': 1, 'name': '...', 'email': '...', 'body': '...'}]
# DEBUG: POST Status Code: 201
# DEBUG: POST Data: {'userId': 1, 'title': 'new post', 'body': 'content', 'id': 101}
# DEBUG: PUT Status Code: 200
# DEBUG: PUT Data: {'userId': 1, 'id': 1, 'title': 'updated post', 'body': 'new content'}
# DEBUG: PATCH Status Code: 200
# DEBUG: PATCH Data: {'userId': 1, 'id': 1, 'title': 'partially updated post', 'body': '...'}
# DEBUG: DELETE Status Code: 200
# DEBUG: DELETE Data: {}
