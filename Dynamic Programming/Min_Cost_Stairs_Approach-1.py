# Minimum Cost Of Stairs Approach No - 1... 

MOD = 1000000007  # Modulo value

# Function to solve the problem using dynamic programming
def solve(n_stairs, i, dp):
    # Base case: If the current position is the top of the stairs, return 1
    if i == n_stairs:
        return 1
    
    # Base case: If the current position is beyond the top of the stairs, return 0
    if i > n_stairs:
        return 0
    
    # If the result for the current position is already computed, return it
    if dp[i] != -1:
        return dp[i]
    
    # Calculate the number of ways to climb the stairs by moving 1 or 2 steps at a time
    dp[i] = (solve(n_stairs, i + 1, dp) + solve(n_stairs, i + 2, dp)) % MOD
    return dp[i]

# Main function
if __name__ == "__main__":
    n_stairs = int(input("Enter the number of stairs: "))  # Input number of stairs
    
    dp = [-1] * (n_stairs + 1)  # Initialize DP table with -1
    ways = solve(n_stairs, 0, dp)  # Calculate the number of ways to climb the stairs
    print("Number of ways to climb the stairs:", ways)
