# Program to perform the Josephus Problem... 

# Function to solve the Josephus Problem
def josephus(n, k):
    # Base Case: If there is only one person left, return 1 (the survivor)
    if n == 1:
        return 1
    else:
        # Recursive Call: Calculate the position of the survivor in the reduced circle
        return (josephus(n - 1, k) + k - 1) % n + 1

# Main function
def main():
    n = 5  # Total number of people in the circle
    k = 2  # Counting interval for elimination
    # Print the position of the survivor
    print("The Answer Is:", josephus(n, k))

# Check if the script is being run directly
if __name__ == "__main__":
    main()  # Call the main function
