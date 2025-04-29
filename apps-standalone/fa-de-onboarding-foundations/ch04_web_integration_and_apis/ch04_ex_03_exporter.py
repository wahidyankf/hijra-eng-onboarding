import pandas as pd  # Import Pandas


def export_to_csv(posts, csv_path):  # Takes posts and CSV path
    """Export posts to CSV."""
    if not posts:  # Check empty
        print("DEBUG: No posts to export")  # Log empty
        return
    df = pd.DataFrame(posts)  # Convert to DataFrame
    df.to_csv(csv_path, index=False)  # Save to CSV
    print(f"DEBUG: Saved to {csv_path}")  # Confirm save


# Test
posts = [{"userId": 1, "id": 1, "title": "sunt aut facere", "body": "quia et suscipit"}]
export_to_csv(posts, "data/test.csv")

# Output:
# DEBUG: Saved to data/test.csv
