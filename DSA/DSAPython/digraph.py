from collections import defaultdict

# This class represents a directed graph using
# adjacency list representation

class diGraph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)
        self.isCyclic = False

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

        # A function used by DFS
    def cycleUtil(self, v, visited, stack):

        if v not in self.graph:
            return False

        # Mark the current node as visited
        visited.add(v)
        stack.add(v)

        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour in stack:
                return True
            elif neighbour not in visited:
                if self.cycleUtil(neighbour, visited, stack) == True:
                    return True
        return False

    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def hasCycle(self):

        # Create a set to store visited vertices
        visited = set()
        stack = set()

        # Call the recursive helper function
        # to print DFS traversal
        for v in self.graph:
            if v not in visited:
                if self.cycleUtil(v, visited, stack) == True:
                    self.isCyclic = True
                    return True
        return False
    
    def topologicalSort(self):

        if self.isCyclic:
            return "not possible due to cycle"
        order = []
        visited = set()

        for v in self.graph:
            if v not in visited:
                self.DFSUtil(v, visited, order)
        return order

        # A function used by DFS
    def DFSUtil(self, v, visited, order):

        if v not in self.graph:
            return False

        # Mark the current node as visited
        # and print it
        visited.add(v)
        order.append(v)

        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited, order)


g = diGraph()
g.addEdge(0, 1)
g.addEdge(1, 2)


g.hasCycle()
if g.isCyclic == True:
    print("Graph has a cycle")
else:
    print("Graph has no cycle")

print(g.topologicalSort())