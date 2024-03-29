# Bellman Ford Algorithm... 

# Bellman-Ford Algorithm
def bellman_ford(n, m, src, dest, edges):
    # Initialize distance array with large values
    dist = [float('inf')] * (n + 1)
    dist[src] = 0  # Distance from source to itself is 0

    # Relax edges repeatedly
    for i in range(1, n + 1):
        for j in range(m):
            u, v, wt = edges[j]
            if dist[u] != float('inf') and dist[u] + wt < dist[v]:
                dist[v] = dist[u] + wt

    # Check for negative weight cycles
    for i in range(m):
        u, v, wt = edges[i]
        if dist[u] != float('inf') and dist[u] + wt < dist[v]:
            return -1  # Negative weight cycle found

    # Return shortest distance to destination
    return dist[dest]

if __name__ == "__main__":
    # Test case
    n = 5  # Number of vertices
    m = 7  # Number of edges
    edges = [
        [1, 2, 4],
        [1, 3, 2],
        [2, 3, 5],
        [2, 4, 10],
        [3, 4, 3],
        [3, 5, 2],
        [4, 5, 4]
    ]
    src = 1   # Source vertex
    dest = 5  # Destination vertex

    # Call Bellman-Ford algorithm
    result = bellman_ford(n, m, src, dest, edges)

    # Print result
    if result != -1:
        print("Shortest distance from", src, "to", dest, "is:", result)
    else:
        print("There is a negative weight cycle in the graph.")
