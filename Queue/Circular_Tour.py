# Circular Tour... 

# Define a function to find the starting petrol pump index
def tour(p, n):
    deficit = 0  # Initialize deficit
    balance = 0  # Initialize balance
    start = 0  # Initialize start index

    for i in range(n):
        balance += p[i][0] - p[i][1]  # Calculate the difference between petrol and distance
        deficit += balance  # Accumulate deficit
        if balance < 0:  # If balance becomes negative, update start index and reset deficit and balance
            start = i + 1
            deficit = 0
            balance = 0

    if deficit + balance >= 0:  # If total deficit and balance at the end are non-negative, a tour is possible
        return start
    else:
        return -1  # No such tour possible

# Main function
if __name__ == "__main__":
    arr = [(4, 6), (6, 5), (7, 3), (4, 5)]  # Petrol pump array with tuples of petrol and distance
    n = len(arr)  # Get the number of petrol pumps
    start = tour(arr, n)  # Find the starting petrol pump index
    if start == -1:
        print("No solution exists.")  # If no solution exists
    else:
        print("Start from petrol pump number:", start)  # Print the starting petrol pump index
