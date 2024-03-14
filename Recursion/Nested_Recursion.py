# Program for Nested Recursion...

# Function to demonstrate nested recursion
def nested_recursion(n):
    if n > 100:  # Base case: if n is greater than 100, return n - 10
        return n - 10

    # Recursive call with a recursive call as parameter
    return nested_recursion(nested_recursion(n + 11))

# Execution starts here
result = nested_recursion(95)  # Call nested_recursion with 95
print("Result:", result)  # Print the result of the nested recursion
