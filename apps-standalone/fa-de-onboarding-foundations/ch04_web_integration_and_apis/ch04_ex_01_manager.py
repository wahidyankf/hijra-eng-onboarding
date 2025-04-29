import requests  # Import requests


def manage_api_data(
    url, new_post, updated_post, partial_update
):  # Takes URL and payloads
    """Perform GET, POST, PUT, PATCH, DELETE requests."""
    # GET
    response_get = requests.get(url)
    if response_get.status_code == 200:
        print(f"DEBUG: GET Fetched {len(response_get.json())} records")
    else:
        print(f"DEBUG: GET Failed: {response_get.status_code}")

    # POST
    response_post = requests.post(url, json=new_post)
    if response_post.status_code == 201:
        print("DEBUG: POST Created post")
    else:
        print(f"DEBUG: POST Failed: {response_post.status_code}")

    # PUT
    response_put = requests.put(f"{url}/1", json=updated_post)
    if response_put.status_code == 200:
        print("DEBUG: PUT Updated post")
    else:
        print(f"DEBUG: PUT Failed: {response_put.status_code}")

    # PATCH
    response_patch = requests.patch(f"{url}/1", json=partial_update)
    if response_patch.status_code == 200:
        print("DEBUG: PATCH Partially updated post")
    else:
        print(f"DEBUG: PATCH Failed: {response_patch.status_code}")

    # DELETE
    response_delete = requests.delete(f"{url}/1")
    if response_delete.status_code == 200:
        print("DEBUG: DELETE Successful")
    else:
        print(f"DEBUG: DELETE Failed: {response_delete.status_code}")


# Test
url = "https://jsonplaceholder.typicode.com/posts"
new_post = {"userId": 1, "title": "new post", "body": "content"}
updated_post = {"userId": 1, "id": 1, "title": "updated post", "body": "new content"}
partial_update = {"title": "partially updated post"}
manage_api_data(url, new_post, updated_post, partial_update)

# Output:
# DEBUG: GET Fetched 100 records
# DEBUG: POST Created post
# DEBUG: PUT Updated post
# DEBUG: PATCH Partially updated post
# DEBUG: DELETE Successful
