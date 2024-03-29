# Depth First Traversal In Graph... 

def dfs(node, visited, adj, component):
    # Depth First Search recursive function
    component.append(node)
    visited[node] = True
    for neighbor in adj[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited, adj, component)

def depth_first_search(v, edges):
    # Building adjacency list from edge list
    adj = {i: [] for i in range(v)}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    ans = []
    visited = {i: False for i in range(v)}
    for i in range(v):
        if not visited[i]:
            component = []
            dfs(i, visited, adj, component)
            ans.append(component)
    return ans

if __name__ == "__main__":
    # Example usage:
    v = 6  # Number of vertices
    edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 4], [3, 5], [4, 5]]

    components = depth_first_search(v, edges)

    # Printing the components
    for component in components:
        print(*component)
