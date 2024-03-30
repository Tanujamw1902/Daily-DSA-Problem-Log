# DP Bottom Up Approach... 

# Function to calculate Fibonacci number using Dynamic Programming (Bottom-up approach)
def fibonacci(n):
    # Initialize a list to store Fibonacci numbers
    dp = [0] * (n + 1)
    
    # Base cases
    dp[0] = 0
    dp[1] = 1
    
    # Calculate Fibonacci numbers bottom-up
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]  # Return the Fibonacci number at position n

# Main function
if __name__ == "__main__":
    n = int(input("Enter the position of Fibonacci number: "))  # Input the position of Fibonacci number
    result = fibonacci(n)  # Calculate Fibonacci number at position n
    print(f"Fibonacci number at position {n}: {result}")  # Output the Fibonacci number at position n
