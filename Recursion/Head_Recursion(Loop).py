# Program for Head Recursion using while loop...

# Function to demonstrate conversion of head recursion into a loop
def count_up(n):
    i = 1  # Initialize a counter variable i with value 1
    while i <= n:  # Loop until i reaches the value of n
        print(i, end=" ")  # Print the current value of i
        i += 1  # Increment i by 1 in each iteration

# Execution starts here
ending_number = 5  # Set the ending number for counting up
count_up(ending_number)  # Call the count_up function with the ending number
