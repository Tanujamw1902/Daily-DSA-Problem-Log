# Minimum Cost Of Stairs Approach No - 5... 

def solve(cost):
    prev2 = cost[0]  # Cost of reaching step 0
    prev1 = cost[1]  # Cost of reaching step 1

    # Iterate from step 2 to n-1
    for i in range(2, len(cost)):
        curr = cost[i] + min(prev1, prev2)  # Calculate the current cost
        prev2 = prev1  # Update prev2 to previous step's cost
        prev1 = curr  # Update prev1 to current step's cost

    # Return the minimum cost of reaching the last step
    return min(prev1, prev2)

if __name__ == "__main__":
    cost = [10, 15, 20, 25, 30]  # Sample costs for each step

    # Calculate the minimum cost of climbing stairs
    min_cost = solve(cost)

    print("Minimum cost of climbing stairs:", min_cost)
