# Program to perform  Palindrome using Recursion...

# Function to check if a number is palindrome
def is_palindrome(n, temp):
    # Base Case: if n becomes 0, return the reversed number (stored in temp)
    if n == 0:
        return temp
    # Main Calculation: Reverse the number
    temp = (temp * 10) + (n % 10)
    # Recursive Call: Move to the next digit of the number
    return is_palindrome(n // 10, temp)

# Main function
def main():
    n = 121  # Define the number to be checked for palindrome
    temp = is_palindrome(n, 0)  # Call the is_palindrome function
    # Check if the reversed number is equal to the original number
    if temp == n:
        print("It is Palindrome")
    else:
        print("It is Not a Palindrome")

# Check if the script is being run directly
if __name__ == "__main__":
    main()  # Call the main function
