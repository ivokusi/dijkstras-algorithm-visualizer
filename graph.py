# Adjency List Implementation of Graph

class Graph:

    def __init__(self, vertices, edges):
        
        # Keys: Node
        # Value: (Weight, Neighbor Node)

        # Create graph from vertices.dat, and edges.dat

        graph = dict()

        with open(vertices, "r") as f1:
            lines = f1.readlines()

        for line in lines:

            if line == "\n":
                continue
            
            vertex = line[:-1]
            graph[vertex] = list()

        with open(edges, "r") as f2:
            lines = f2.readlines()

        for line in lines:

            if line == "\n":
                continue

            src, dest, weight = line.split()
            graph[src].append((dest, int(weight)))

        self.graph = graph

    def get_vertices(self):
        return list(self.graph.keys())

    def get_neighbors(self, src):
        return self.graph[src]

