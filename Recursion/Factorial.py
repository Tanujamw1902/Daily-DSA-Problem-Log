# Program for Factorial...

# Recursive function to calculate factorial
def recursive_factorial(n):
    # Base case: if n equals 1, return 1
    if n == 1:
        return n
    else:
        # Recursive call to calculate factorial
        return n * recursive_factorial(n - 1)

# Input number for which factorial will be calculated
num = 6

# Check if the input is valid
if num < 0:
    print("Invalid input! Please enter a positive number.")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    # Calculate and print factorial of the input number
    print("Factorial of", num, "is", recursive_factorial(num))
