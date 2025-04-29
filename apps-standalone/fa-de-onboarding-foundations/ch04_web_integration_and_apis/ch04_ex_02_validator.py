import yaml  # Import YAML
import utils  # Import utils


def read_config(config_path):  # Read config
    with open(config_path, "r") as file:
        return yaml.safe_load(file)


def validate_posts(posts, config):  # Takes posts and config
    """Validate posts using utils.py."""
    valid_posts = []
    for post in posts:
        if utils.validate_post(post, config):
            valid_posts.append(post)
        else:
            print(f"DEBUG: Invalid post: {post}")  # Debug
    print(f"DEBUG: Valid posts: {len(valid_posts)}")  # Debug
    return valid_posts


# Test
config = read_config("data/config.yaml")
posts = [
    {"userId": 1, "id": 1, "title": "sunt aut facere", "body": "quia et suscipit"},
    {"userId": 0, "id": 2, "title": "qui est esse", "body": "est rerum tempore"},
]
print(validate_posts(posts, config))

# Output:
# DEBUG: Validating post: {'userId': 1, ...}
# DEBUG: Validating post: {'userId': 0, ...}
# DEBUG: Invalid: invalid userId: {'userId': 0, ...}
# DEBUG: Valid posts: 1
# [{'userId': 1, ...}]
