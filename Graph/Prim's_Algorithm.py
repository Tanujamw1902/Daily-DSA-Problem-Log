# Prim's Algorithm... 

import heapq


def calculate_prims_mst(n, m, edges):
    # Adjacency list
    adj = {i: [] for i in range(1, n + 1)}
    
    # Making Adjacency list
    for edge in edges:
        u, v, w = edge
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Initializing important variables
    key = [float('inf')] * (n + 1)  # Key values for vertices
    parent = [-1] * (n + 1)          # Parent array to store MST
    mst = [False] * (n + 1)          # To keep track of vertices in MST
    
    # Start with the first vertex
    key[1] = 0
    
    # Construct MST
    for _ in range(1, n):
        u = -1
        min_key = float('inf')
        
        # Find vertex with minimum key value
        for v in range(1, n + 1):
            if not mst[v] and key[v] < min_key:
                min_key = key[v]
                u = v
        
        # Add the selected vertex to MST
        mst[u] = True
        
        # Update key values and parent for adjacent vertices
        for v, w in adj[u]:
            if not mst[v] and w < key[v]:
                parent[v] = u
                key[v] = w
    
    # Construct MST edges
    mst_edges = []
    for v in range(2, n + 1):
        mst_edges.append(((parent[v], v), key[v]))
    
    return mst_edges

if __name__ == "__main__":
    # Test case
    n = 5  # Number of vertices
    m = 7  # Number of edges
    edges = [
        (1, 2, 4),
        (1, 3, 2),
        (2, 3, 5),
        (2, 4, 10),
        (3, 4, 3),
        (3, 5, 2),
        (4, 5, 4)
    ]

    # Calculate MST edges using Prim's algorithm
    mst_edges = calculate_prims_mst(n, m, edges)

    # Print MST edges
    print("Minimum Spanning Tree Edges:")
    for edge in mst_edges:
        print(f"{edge[0][0]} - {edge[0][1]} : {edge[1]}")
