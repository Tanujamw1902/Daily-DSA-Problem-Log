# Program for Tail Recursion...

# Function to demonstrate tail recursion
def countdown(n):
    if n > 0:  # Base case: if n is greater than 0, continue recursion
        print(n, end=" ")  # Print the current value of n
        countdown(n - 1)  # Tail recursive call with n decremented by 1

# Execution starts here
starting_number = 5  # Set the starting number for countdown
countdown(starting_number)  # Call the countdown function with the starting number
