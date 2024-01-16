


class DirectedGraph:
    def _init__(self):
        self.graph = {}

    def add_edge(self, node_from, node_to):
        if node_from not in self.graph:
            self.graph[node_from] = []
        if node_to not in self.graph:
            self.graph[node_to] = []
        self.graph[node_from].append(node_to)