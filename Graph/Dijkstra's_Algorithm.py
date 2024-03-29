# Dijkstra's Algorithm... 

import heapq


def dijkstra(graph, vertices, edges, source):
    # Build adjacency list from the given edge list
    adj = {i: [] for i in range(vertices)}
    for u, v, w in graph:
        adj[u].append((v, w))
        adj[v].append((u, w))

    # Initialize distances with infinity
    distances = [float('inf')] * vertices
    distances[source] = 0

    # Priority queue to select node with minimum distance
    pq = [(0, source)]

    while pq:
        node_distance, node = heapq.heappop(pq)

        # Ignore if already visited
        if node_distance > distances[node]:
            continue

        # Explore neighbors
        for neighbor, weight in adj[node]:
            distance = node_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Function to print shortest paths
def print_shortest_paths(shortest_distances, source):
    print("Shortest paths visualization:")
    for i, distance in enumerate(shortest_distances):
        node = chr(ord('A') + i)  # Assuming nodes are represented by characters starting from 'A'
        if i == source:
            print(node, "->", node, ":", 0)
        elif distance == float('inf'):
            print(node, "->", node, ":", "Not reachable")
        else:
            print(chr(ord('A') + source), "->", node, ":", distance)

if __name__ == "__main__":
    # Test case
    graph = [
        [0, 1, 4], [0, 7, 8], [1, 2, 8], [1, 7, 11], [2, 3, 7],
        [2, 8, 2], [2, 5, 4], [3, 4, 9], [3, 5, 14], [4, 5, 10],
        [5, 6, 2], [6, 7, 1], [6, 8, 6], [7, 8, 7]
    ]
    vertices = 9
    edges = 14
    source = 0

    result = dijkstra(graph, vertices, edges, source)
    print_shortest_paths(result, source)
