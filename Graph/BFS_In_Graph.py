# Breadth First Traversal In Graph... 

from collections import defaultdict, deque


def prepare_adj_list(adj_list, edges):
    # Function to prepare adjacency list from edge list
    for u, v in edges:
        adj_list[u].add(v)
        adj_list[v].add(u)

def bfs(adj_list, visited, ans, node):
    # Breadth First Traversal
    q = deque()
    q.append(node)
    visited[node] = True

    while q:
        front_node = q.popleft()
        ans.append(front_node)

        for neighbor in adj_list[front_node]:
            if not visited[neighbor]:
                q.append(neighbor)
                visited[neighbor] = True

def bfs_traversal(vertex, edges):
    # Initialize adjacency list, visited map, and result list
    adj_list = defaultdict(set)
    visited = defaultdict(bool)
    ans = []

    # Prepare adjacency list from edge list
    prepare_adj_list(adj_list, edges)

    # Perform BFS traversal for each unvisited node
    for i in range(vertex):
        if not visited[i]:
            bfs(adj_list, visited, ans, i)

    # Print the BFS traversal result
    print("Breadth First Traversal:", *ans)

if __name__ == "__main__":
    # Define the number of vertices
    vertex = 6

    # Define the edges of the graph
    edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (3, 5), (4, 5)]

    # Call the BFS traversal function
    bfs_traversal(vertex, edges)
