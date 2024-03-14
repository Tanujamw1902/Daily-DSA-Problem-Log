# Program for Head Recursion...

# Function to demonstrate head recursion
def count_up(n):
    if n > 0:  # Base case: if n is greater than 0, continue recursion
        count_up(n - 1)  # Head recursive call with n decremented by 1

        print(n, end=" ")  # Print the current value of n after recursive call

# Execution starts here
starting_number = 5  # Set the starting number for counting up
count_up(starting_number)  # Call the count_up function with the starting number
