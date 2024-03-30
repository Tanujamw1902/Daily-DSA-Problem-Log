# Minimum Cost Of Stairs Approach No - 4... 

# Function to solve the problem using dynamic programming
def solve(cost):
    n = len(cost)
    dp = [0] * (n + 1)
    dp[0] = cost[0]
    dp[1] = cost[1]

    # Iterate from step 2 to n
    for i in range(2, n):
        # Calculate the minimum cost of climbing the stairs from the current position
        dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
    
    # The minimum cost of climbing the stairs to reach the nth step
    return dp[n - 1]  # Return the cost of reaching the nth step

# Main function
if __name__ == "__main__":
    cost = [10, 15, 20, 25, 30]  # Sample costs for each step
    
    # Calculate the minimum cost of climbing stairs
    min_cost = solve(cost)
    
    print("Minimum cost of climbing stairs:", min_cost)
