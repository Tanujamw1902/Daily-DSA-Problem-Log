# Graph Using Adjacency List... 

class Graph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v, direction):
        if u not in self.adj:
            self.adj[u] = []
        self.adj[u].append(v)
        if not direction:
            if v not in self.adj:
                self.adj[v] = []
            self.adj[v].append(u)

    def print_adj_list(self):
        for vertex, neighbors in self.adj.items():
            print(f"{vertex} -> {' , '.join(map(str, neighbors))}")

if __name__ == "__main__":
    # Input number of nodes and edges
    n = int(input("Enter the number of nodes: "))
    m = int(input("Enter the number of edges: "))

    g = Graph()

    # Input edges and add them to the graph
    print("Enter edges (u v):")
    for _ in range(m):
        u, v = map(int, input().split())
        g.add_edge(u, v, direction=False)

    # Print the adjacency list representation of the graph
    print("Adjacency List:")
    g.print_adj_list()
