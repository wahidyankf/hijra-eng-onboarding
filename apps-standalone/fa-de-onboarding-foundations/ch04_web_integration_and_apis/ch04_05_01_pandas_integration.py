import requests  # Import requests
import pandas as pd  # Import Pandas
import utils  # Import utils
import yaml  # Import YAML

# Load config
with open("data/config.yaml", "r") as file:
    config = yaml.safe_load(file)

# Fetch and validate posts
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
if response.status_code == 200:
    posts = response.json()
    valid_posts = [p for p in posts if utils.validate_post(p, config)]
    print(f"DEBUG: Valid posts: {len(valid_posts)}")  # Debug
else:
    valid_posts = []
    print("DEBUG: Fetch failed:", response.status_code)

print("--------")

# Convert to DataFrame
df = pd.DataFrame(valid_posts)
print("DEBUG: DataFrame:")  # Debug
print(df.head())

# Save to CSV
csv_path = "data/posts.csv"
df.to_csv(csv_path, index=False)
print(f"DEBUG: Saved to {csv_path}")

# Expected Output:
# DEBUG: Valid posts: 100
# DEBUG: DataFrame:
#    userId  id                                              title                                               body
# 0       1   1  sunt aut facere repellat provident occaecati e...  quia et suscipit\nsuscipit recusandae consequun...
# 1       1   2                                        qui est esse  est rerum tempore vitae\nsequi sint nihil repre...
# ...
# DEBUG: Saved to data/posts.csv
