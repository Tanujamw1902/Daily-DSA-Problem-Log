# Program for Fibonacci Series...

# Function to calculate the nth Fibonacci number recursively
def recursive_fibonacci(n):
    # Base case: if n is 0 or 1, return n
    if n <= 1:
        return n
    else:
        # Recursive call to calculate Fibonacci number
        return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))

# Number of terms in the Fibonacci series
n_terms = 10

# Check if the number of terms is valid
if n_terms <= 0:
    print("Invalid input! Please input a positive value")
else:
    print("Fibonacci series:")
    # Generate and print Fibonacci series up to n_terms
    for i in range(n_terms):
        print(recursive_fibonacci(i))
