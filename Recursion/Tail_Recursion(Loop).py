# Program for Tail Recursion using while loop...

# Function to demonstrate conversion of tail recursion into a loop
def countdown(y):
    while y > 0:  # Loop until y is greater than 0
        print(y, end=" ")  # Print the current value of y
        y -= 1  # Decrement y by 1 in each iteration

# Execution starts here
starting_number = 5  # Set the starting number for countdown
countdown(starting_number)  # Call the countdown function with the starting number
