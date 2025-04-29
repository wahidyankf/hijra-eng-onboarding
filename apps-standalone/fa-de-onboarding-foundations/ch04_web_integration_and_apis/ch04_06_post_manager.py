import requests  # For API requests
import pandas as pd  # For DataFrame operations
import yaml  # For YAML parsing
import os  # For file existence check
import utils


# Define function to read YAML configuration
def read_config(config_path):  # Takes config file path
    """Read YAML configuration."""
    print(f"DEBUG: Opening config: {config_path}")  # Debug
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)  # Parse YAML
    print(f"DEBUG: Loaded config: {config}")  # Debug
    return config


# Define function to fetch data from API
def fetch_data(url, method="get", data=None):  # Takes URL, method, and optional data
    """Perform HTTP request (GET, POST, PUT, PATCH, DELETE)."""
    print(f"DEBUG: Performing {method.upper()} request to: {url}")  # Debug
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
        print(f"DEBUG: Invalid method: {method}")
        return None
    print(f"DEBUG: Status Code: {response.status_code}")  # Debug
    if response.status_code in (200, 201, 204):
        data = response.json() if response.content else {}
        print(f"DEBUG: Response Data: {data}")  # Debug
        return data
    print(f"DEBUG: Request failed: {response.status_code}")  # Log failure
    return None


# Define function to validate and filter posts
def validate_data(posts, config):  # Takes posts and config
    """Validate posts using utils.py and summarize errors."""
    if not posts:
        return []
    valid_posts = []
    invalid_count = 0
    error_summary = {
        "missing_field": 0,
        "invalid_user_id": 0,
        "invalid_id": 0,
        "empty_title_or_body": 0,
    }
    for post in posts:
        required_fields = config["required_fields"]
        min_user_id = config["min_user_id"]
        min_id = config["min_id"]

        # Check required fields
        for field in required_fields:
            if field not in post or not post[field]:
                print(
                    f"DEBUG: Invalid: missing or empty {field}: {post}"
                )  # Log invalid
                error_summary["missing_field"] += 1
                invalid_count += 1
                continue

        # Validate userId
        user_id = post["userId"]
        if not utils.is_integer(user_id) or int(user_id) < min_user_id:
            print(f"DEBUG: Invalid: invalid userId: {post}")  # Log invalid
            error_summary["invalid_user_id"] += 1
            invalid_count += 1
            continue

        # Validate id
        post_id = post["id"]
        if not utils.is_integer(post_id) or int(post_id) < min_id:
            print(f"DEBUG: Invalid: invalid id: {post}")  # Log invalid
            error_summary["invalid_id"] += 1
            invalid_count += 1
            continue

        # Validate title and body
        title = utils.clean_string(post["title"])
        body = utils.clean_string(post["body"])
        if not title or not body:
            print(f"DEBUG: Invalid: empty title or body: {post}")  # Log invalid
            error_summary["empty_title_or_body"] += 1
            invalid_count += 1
            continue

        valid_posts.append(post)

    print(f"DEBUG: Valid posts: {len(valid_posts)}")  # Debug
    print(f"DEBUG: Invalid posts: {invalid_count}")  # Debug
    print("DEBUG: Validation Errors:")
    for error_type, count in error_summary.items():
        print(f"  {error_type}: {count}")
    return valid_posts


# Define function to save to CSV
def save_to_csv(posts, csv_path):  # Takes posts and CSV path
    """Save valid posts to CSV."""
    if not posts:  # Check for empty data
        print("DEBUG: No valid posts to save")  # Log empty
        return
    df = pd.DataFrame(posts)  # Convert to DataFrame
    print("DEBUG: DataFrame:")  # Debug
    print(df.head())  # Show first rows
    df.to_csv(csv_path, index=False)  # Save to CSV
    print(f"DEBUG: Saved to {csv_path}")  # Confirm save
    print(f"DEBUG: File exists: {os.path.exists(csv_path)}")  # Confirm file creation


# Define main function
def main():  # No parameters
    """Main function to manage posts."""
    base_url = "https://jsonplaceholder.typicode.com"
    config_path = "data/config.yaml"  # YAML path
    csv_path = "data/posts.csv"  # CSV output path

    config = read_config(config_path)  # Read config

    # GET: Fetch posts
    posts = fetch_data(f"{base_url}/posts", method="get")
    if posts:
        valid_posts = validate_data(posts, config)
        save_to_csv(valid_posts, csv_path)

    # POST: Create a new post
    new_post = {"userId": 1, "title": "new post", "body": "content"}
    created_post = fetch_data(f"{base_url}/posts", method="post", data=new_post)
    if created_post:
        print(
            "DEBUG: Created post validated:", utils.validate_post(created_post, config)
        )

    # PUT: Update a post
    updated_post = {
        "userId": 1,
        "id": 1,
        "title": "updated post",
        "body": "new content",
    }
    updated_result = fetch_data(f"{base_url}/posts/1", method="put", data=updated_post)
    if updated_result:
        print(
            "DEBUG: Updated post validated:",
            utils.validate_post(updated_result, config),
        )

    # PATCH: Partially update a post
    partial_update = {"title": "partially updated post"}
    patched_result = fetch_data(
        f"{base_url}/posts/1", method="patch", data=partial_update
    )
    if patched_result:
        print(
            "DEBUG: Patched post validated:",
            utils.validate_post(patched_result, config),
        )

    # DELETE: Delete a post
    delete_result = fetch_data(f"{base_url}/posts/1", method="delete")
    if delete_result is not None:
        print("DEBUG: Delete operation successful")

    # Output report for GET operation
    if posts:
        print("\nPost Report:")
        print(f"DEBUG: Total Records Fetched: {len(posts)}")
        print(f"DEBUG: Valid Posts: {len(valid_posts)}")
        print(f"DEBUG: Invalid Posts: {len(posts) - len(valid_posts)}")
        print("DEBUG: Processing completed")


if __name__ == "__main__":
    main()  # Run main function
