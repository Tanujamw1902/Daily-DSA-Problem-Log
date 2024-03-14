# Program to print n to 1...

# Function to print numbers from N to 1 in reverse order
def print_reverse(n):
    # Base condition for termination: if n is less than or equal to 0, return
    if n <= 0:
        return
    else:
        # Print the current number
        print(n, end=" ")  # Printing with a space after each number
        # Recursive call to print numbers from N-1 to 1
        print_reverse(n - 1)

# Main function
def main():
    n = 5  # Define the value of N
    print_reverse(n)  # Call the print_reverse function with N as argument

# Check if the script is being run directly
if __name__ == "__main__":
    main()  # Call the main function
