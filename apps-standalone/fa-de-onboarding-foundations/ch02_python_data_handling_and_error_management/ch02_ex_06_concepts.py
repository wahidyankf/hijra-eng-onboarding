def explain_module_benefits(output_path):  # Takes output file path
    """Write explanation of module benefits."""
    explanation = (
        "Using utils.py for validation functions like clean_string and is_numeric "
        "improves code maintainability by organizing reusable code in one place, "
        "reducing duplication across scripts. This modular design makes it easier "
        "to update validation logic, such as changing decimal rules, without modifying "
        "multiple files. It also enhances readability and supports Hijra Group’s scalable "
        "pipelines by keeping main scripts focused on processing logic."
    )
    file = open(output_path, "w")  # Open file
    file.write(explanation)  # Write explanation
    file.close()  # Close file
    print(f"Explanation saved to {output_path}")  # Confirm save
    return explanation  # Return explanation


# Test
print(explain_module_benefits("ex6_concepts.txt"))  # Call function

# Output:
# Explanation saved to ex6_concepts.txt
# Using utils.py for validation functions like clean_string and is_numeric ...
