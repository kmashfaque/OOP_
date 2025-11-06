class Graph:
    def __init__(self):
        self.graph = {}
        self.directed = True


    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)

        if not self.directed:
            self.graph[v].append(u)

    def from_edge_list(self, edges):
        for u, v in edges:
            self.add_edge(u, v)
    
    def to_edge_list(self):
        edges = []
        seen = set()

        for u in self.graph:
            for v in self.graph[u]:
                if (u, v) not in seen:
                    edges.append((u, v))
                    seen.add((u, v))
        return edges
    
    # def print_edges(self):
    #     print("Edges in the graph: ")

    #     visited = set()

    #     for node in self.graph:
    #         for neighbor in self.graph[node]:
    #             if (neighbor, node) not in visited:
    #                 print(f"{node} -->> {neighbor}")
    #                 visited.add((node,neighbor))

    def is_connected(self, u, v):
        return u in self.graph and v in self.graph[u]

    def print_adjuscency_list(self):
        print("adjuscency list")
        for node in self.graph:
            print(f"{node}: {self.graph[node]}")


edges = [(1,2), (1, 3), (2,4), (3,4), (4,5)]
g = Graph()
# g.add_edge(1, 2)
# g.add_edge(2, 1)
# g.add_edge(1, 3)
# g.add_edge(2, 4)
# g.add_edge(3, 4)
# g.add_edge(4, 5)
g.from_edge_list(edges)
g.to_edge_list()
print("Is 1 ==> 3 connected? --> ",g.is_connected(1,3))
g.print_adjuscency_list()                   