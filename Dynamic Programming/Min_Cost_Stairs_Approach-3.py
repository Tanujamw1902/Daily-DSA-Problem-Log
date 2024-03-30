#  Minimum Cost Of Stairs Approach No - 3... 

import sys


# Function to solve the problem using dynamic programming
def solve(cost, n, dp):
    # Base cases
    if n == 0:
        return cost[0]
    if n == 1:
        return cost[1]
    
    # If the result for the current position is already computed, return it
    if dp[n] != -1:
        return dp[n]
    
    # Calculate the minimum cost of climbing the stairs from the current position
    dp[n] = cost[n] + min(solve(cost, n - 1, dp), solve(cost, n - 2, dp))
    return dp[n]

# Main function
if __name__ == "__main__":
    cost = [10, 15, 20, 25, 30]  # Sample costs for each step
    
    n = len(cost)
    dp = [-1] * n  # Memoization table to store computed results, initialized with -1
    
    # Calculate the minimum cost of climbing stairs starting from step n-1 or n-2, depending on the problem
    min_cost = min(solve(cost, n - 1, dp), solve(cost, n - 2, dp))
    
    print("Minimum cost of climbing stairs:", min_cost)
