# Program to perform Sum of Digits using Recursion...

# Function to find the sum of digits of a given number
def sum_of_digits(n):
    # Base Case: if n becomes 0, return 0
    if n == 0:
        return 0
    # Recursive Call: Add the last digit of n to the sum of digits of the remaining number
    return (n % 10) + sum_of_digits(n // 10)

# Main function
def main():
    n = 121  # Define the number for which the sum of digits will be calculated
    print(sum_of_digits(n))  # Print the sum of digits of the number

# Check if the script is being run directly
if __name__ == "__main__":
    main()  # Call the main function
