# Min Cost Of Ropes... 

import heapq  # Import the heapq module for the priority queue


def min_cost(arr):
    # Create a min-heap (priority queue) with the elements of the array
    heapq.heapify(arr)
    
    cost = 0
    
    # Continue until there is only one rope left in the priority queue
    while len(arr) > 1:
        # Extract the two smallest ropes
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)
        
        # Calculate the sum of the two ropes
        rope_sum = a + b
        
        # Add the sum to the total cost
        cost += rope_sum
        
        # Push the sum back to the priority queue
        heapq.heappush(arr, rope_sum)
    
    # Return the minimum cost
    return cost

# Example usage
arr = [4, 3, 2, 6]
print("Minimum cost of joining ropes:", min_cost(arr))
