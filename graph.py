class Graph:
    def __init__(self):
        self.graph = {}

    # def add_node(self, node):
    #     if node not in self.graph:
    #         self.graph[node] = []

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def print_edges(self):
        print("Edges in the graph: ")

        visited = set()

        for node in self.graph:
            for neighbor in self.graph[node]:
                if (neighbor, node) not in visited:
                    print(f"{node} -->> {neighbor}")
                    visited.add((node,neighbor))


g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.add_edge(4, 5)

g.print_edges()                   