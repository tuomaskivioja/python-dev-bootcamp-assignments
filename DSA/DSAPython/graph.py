# Python3 program to print DFS traversal
# from a given graph
from collections import defaultdict

# This class represents a undirected graph using
# adjacency list representation


class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # A function used by DFS
    def DFSUtil(self, v, visited):

        # Mark the current node as visited
        # and print it
        visited.add(v)
        print(v, end=' ')

        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, v):

        # Create a set to store visited vertices
        visited = set()

        # Call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(v, visited)

    def connectedGraph(self, s):

        visited = set()

        self.DFSUtil(s, visited)
        for n in self.graph:
            if n not in visited:
                return False
        return True
    
    def BFS(self, v):

        visited = set()

        queue = []
        self.BFSUtil(v, visited, queue)

    def BFSUtil(self, v, visited, queue): 
        visited.add(v)
        print(v)
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(v)
                s = queue.pop(0)
                self.BFSUtil(s, visited, queue)

    # Python implementation to find the
    # shortest path in the graph using
    # dictionaries

    # Function to find the shortest
    # path between two nodes of a graph
    def BFS_SP(self, start, goal):
        explored = []
        
        # Queue for traversing the
        # graph in the BFS
        queue = [[start]]
        
        # If the desired node is
        # reached
        if start == goal:
            print("Same Node")
            return
        
        # Loop to traverse the graph
        # with the help of the queue
        while queue:
            path = queue.pop(0)
            node = path[-1]
            
            # Condition to check if the
            # current node is not visited
            if node not in explored:
                neighbours = self.graph[node]
                
                # Loop to iterate over the
                # neighbours of the node
                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
                    
                    # Condition to check if the
                    # neighbour node is the goal
                    if neighbour == goal:
                        print("Shortest path = ", *new_path)
                        return
                explored.append(node)

        # Condition when the nodes
        # are not connected
        print("So sorry, but a connecting"\
                    "path doesn't exist :(")
        return


# Driver code


# Create a graph given
# in the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.addEdge(4, 7)


print("Following is BFS from (starting from vertex 2)")
g.BFS(1)
g.BFS_SP(0, 3)

# This code is contributed by Neelam Yadav
