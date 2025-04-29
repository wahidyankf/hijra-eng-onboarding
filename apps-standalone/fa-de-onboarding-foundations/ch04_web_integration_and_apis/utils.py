def clean_string(s):  # Clean string
    """Strip whitespace from string."""
    return s.strip() if isinstance(s, str) else ""


def is_integer(x):  # Check if value is integer
    """Check if value is an integer."""
    return isinstance(x, int) or (isinstance(x, str) and x.lstrip("-").isdigit())


def validate_post(post, config):  # Validate post
    """Validate post based on config rules."""
    required_fields = config["required_fields"]  # Get required fields
    min_user_id = config["min_user_id"]  # Get minimum user ID
    min_id = config["min_id"]  # Get minimum ID

    print(f"DEBUG: Validating post: {post}")  # Debug
    # Check required fields
    for field in required_fields:
        if field not in post or not post[field]:
            print(f"DEBUG: Invalid: missing or empty {field}: {post}")  # Log invalid
            return False

    # Validate userId
    user_id = post["userId"]
    if not is_integer(user_id) or int(user_id) < min_user_id:
        print(f"DEBUG: Invalid: invalid userId: {post}")  # Log invalid
        return False

    # Validate id
    post_id = post["id"]
    if not is_integer(post_id) or int(post_id) < min_id:
        print(f"DEBUG: Invalid: invalid id: {post}")  # Log invalid
        return False

    # Validate title and body (ensure non-empty after cleaning)
    title = clean_string(post["title"])
    body = clean_string(post["body"])
    if not title or not body:
        print(f"DEBUG: Invalid: empty title or body: {post}")  # Log invalid
        return False

    return True  # Valid post


# Example: Valid GET response
config = {
    "required_fields": ["userId", "id", "title", "body"],
    "min_user_id": 1,
    "min_id": 1,
}
valid_post = {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere",
    "body": "quia et suscipit",
}
print(validate_post(valid_post, config))  # True
# Example: Invalid GET response
invalid_post = {"userId": 0, "id": 2, "title": "", "body": ""}
print(validate_post(invalid_post, config))  # False
# Example: Valid POST payload
post_payload = {"userId": 1, "title": "new post", "body": "content"}
print(validate_post(post_payload, config))  # True
