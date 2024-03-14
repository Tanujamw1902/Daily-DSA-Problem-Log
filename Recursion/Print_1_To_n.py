# Program to print 1 to n...

# Function to print numbers from 1 to n without using loops
def print_numbers(n):
    # Base condition for termination: if n is less than or equal to 0, return
    if n <= 0:
        return
    else:
        # Recursive call to print numbers from 1 to n-1
        print_numbers(n - 1)
        # Print the current number
        print(n, end=" ")  # Printing with a space after each number

# Main function
def main():
    n = 5  # Define the value of n
    print_numbers(n)  # Call the print_numbers function with n as argument

# Check if the script is being run directly
if __name__ == "__main__":
    main()  # Call the main function
