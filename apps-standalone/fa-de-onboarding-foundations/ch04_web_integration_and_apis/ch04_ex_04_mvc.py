import requests  # Import requests
import pandas as pd  # Import Pandas
import yaml  # Import YAML
import utils  # Import utils


def read_config(config_path):  # Model
    with open(config_path, "r") as file:
        return yaml.safe_load(file)


def fetch_data(url, method="get", data=None):  # Model
    if method == "get":
        response = requests.get(url)
    elif method == "post":
        response = requests.post(url, json=data)
    elif method == "put":
        response = requests.put(url, json=data)
    elif method == "patch":
        response = requests.patch(url, json=data)
    elif method == "delete":
        response = requests.delete(url)
    else:
        return None
    if response.status_code in (200, 201, 204):
        return response.json() if response.content else {}
    return None


def validate_data(posts, config):  # Model
    return [p for p in posts if utils.validate_post(p, config)]


def save_to_csv(posts, csv_path):  # View
    if posts:
        pd.DataFrame(posts).to_csv(csv_path, index=False)
        print(f"DEBUG: Saved to {csv_path}")


def manage_posts(
    url, config_path, csv_path, new_post, updated_post, partial_update
):  # Controller
    config = read_config(config_path)  # Model
    # GET
    posts = fetch_data(url, method="get")
    if posts:
        valid_posts = validate_data(posts, config)
        save_to_csv(valid_posts, csv_path)
    # POST
    created_post = fetch_data(url, method="post", data=new_post)
    # PUT
    updated_result = fetch_data(f"{url}/1", method="put", data=updated_post)
    # PATCH
    patched_result = fetch_data(f"{url}/1", method="patch", data=partial_update)
    # DELETE
    delete_result = fetch_data(f"{url}/1", method="delete")
    print(f"DEBUG: Processed {len(valid_posts if posts else [])} valid posts")


# Test
url = "https://jsonplaceholder.typicode.com/posts"
config_path = "data/config.yaml"
csv_path = "data/test.csv"
new_post = {"userId": 1, "title": "new post", "body": "content"}
updated_post = {"userId": 1, "id": 1, "title": "updated post", "body": "new content"}
partial_update = {"title": "partially updated post"}
manage_posts(url, config_path, csv_path, new_post, updated_post, partial_update)

# Output:
# DEBUG: Saved to data/test.csv
# DEBUG: Processed 98 valid posts
