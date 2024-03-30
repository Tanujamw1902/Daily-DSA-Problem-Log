# DP Top Down Approach... 

# Function to calculate Fibonacci number using Dynamic Programming (Top-down approach)
def fib(n, dp):
    # Base cases
    if n <= 1:
        return n
    
    # If already calculated, return the result from dp table
    if dp[n] != -1:
        return dp[n]
    
    # Recursive call to calculate Fibonacci number
    dp[n] = fib(n - 1, dp) + fib(n - 2, dp)
    return dp[n]

# Main function
if __name__ == "__main__":
    n = 10  # Calculate Fibonacci number for n
    dp = [-1] * (n + 1)  # Initialize DP table with -1
    dp[0] = 0
    dp[1] = 1
    
    # Calculate Fibonacci number at position n
    result = fib(n, dp)
    print(f"Fibonacci number at position {n}: {result}")
