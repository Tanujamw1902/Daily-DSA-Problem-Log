# Program for Tree Recursion...

# Function to demonstrate tree recursion
def tree_recursion(n):
    if n > 0:  # Base case: if n is greater than 0, continue recursion
        print(n, end=" ")  # Print the current value of n

        # First recursive call
        tree_recursion(n - 1)  # Call tree_recursion with n decremented by 1
        
        # Second recursive call
        tree_recursion(n - 1)  # Call tree_recursion with n decremented by 1 again

# Execution starts here
starting_number = 3  # Set the starting number for tree recursion
tree_recursion(starting_number)  # Call the tree_recursion function with the starting number
