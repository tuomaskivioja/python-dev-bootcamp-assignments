
class WeightedUndirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:
            self.graph[node1] = []
        if node2 not in self.graph:
            self.graph[node2] = []

        # Add an edge from node_from to node_to
        self.graph[node1].append((node2, weight))

        # Add an edge from node_to to node_from
        self.graph[node2].append((node1, weight))
