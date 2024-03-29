# Kruskal's Algorithm... 

def make_set(parent, rank, n):
    for i in range(n):
        parent[i] = i
        rank[i] = 0

def find_parent(parent, node):
    if parent[node] == node:
        return node
    parent[node] = find_parent(parent, parent[node])
    return parent[node]

def union_set(u, v, parent, rank):
    u = find_parent(parent, u)
    v = find_parent(parent, v)
    if rank[u] < rank[v]:
        parent[u] = v
    elif rank[v] < rank[u]:
        parent[v] = u
    else:
        parent[v] = u
        rank[u] += 1

def kruskal(edges, n):
    edges.sort(key=lambda x: x[2])  # Sort edges by weight
    parent = [0] * n
    rank = [0] * n
    make_set(parent, rank, n)
    min_weight = 0
    for edge in edges:
        u, v, wt = edge
        if find_parent(parent, u) != find_parent(parent, v):
            min_weight += wt
            union_set(u, v, parent, rank)
    return min_weight

if __name__ == "__main__":
    # Test case
    n = 6  # Number of vertices
    edges = [
        [0, 1, 4],
        [0, 2, 3],
        [1, 2, 1],
        [1, 3, 2],
        [2, 3, 4],
        [3, 4, 2],
        [4, 5, 6]
    ]

    # Calculate minimum spanning tree weight
    min_weight = kruskal(edges, n)
    print("Minimum Spanning Tree Weight:", min_weight)
