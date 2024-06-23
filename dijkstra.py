from graph import Graph
import heapq

class Dijkstra:

    def __init__(self, vertices, edges, start):
       
        # Keys: Node
        # Values: (Parent Node, Cost)

        self.table = dict()
        graph = Graph(vertices, edges)
        
        vertices = graph.get_vertices()
        for vertex in vertices:
            self.table[vertex] = ("-", float("inf"))
        vertices.remove(start)

        self.table[start] = ("-", 0)
        
        # Heap Item: (Cost, Node)

        heap = list()

        for (neighbor, cost) in graph.get_neighbors(start):
            self.table[neighbor] = (start, cost)
            heap.append((cost, neighbor))

        while vertices:
            
            (vertex_cost, vertex) = heapq.heappop(heap)
            
            for (neighbor, cost) in graph.get_neighbors(vertex):
                
                (_, current_cost) = self.table[neighbor]
                new_cost = vertex_cost + cost

                if current_cost == float("inf") or new_cost < current_cost:
                    self.table[neighbor] = (vertex, new_cost)

                if neighbor in vertices:
                    heap.append((new_cost, neighbor))

            vertices.remove(vertex)

    def shortest_path(self, end):

        path = list()

        vertex = end
        while vertex != "-":
            path.append(vertex)
            vertex = self.table[vertex][0]

        return (self.table[end][1], path[::-1])

