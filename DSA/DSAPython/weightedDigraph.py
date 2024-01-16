from collections import defaultdict

class Node:

    def __init__(self, v, d):
        self.v = v
        self.dist = d
        self.next = None

class PQ:
    def __init__(self, empty=True):
        self.queue = Node
        self.empty = empty
    
    def put(self, node):
        if self.isEmpty():
            self.queue = node
            self.empty = False
            return
        if self.queue.dist > node.dist:
            node.next = self.queue
            self.queue = node
            return
        next = self.queue.next
        curr = self.queue
        while next != None:
            if next.dist > node.dist:
               break
            curr = next
            next = next.next
        node.next = next
        curr.next = node
    
    def remove(self):
        if self.queue == None:
            return None
        e = self.queue
        self.queue = self.queue.next
        return e
    
    def contains(self, w):
        if self.queue == None:
            return False
        if self.queue.v == w:
            return True
        next = self.queue.next
        while next != None:
            if next.v == w:
                return True
            next = next.next
        return False
    
    def change(self, w, dist):
        if self.queue.v == w:
            self.queue.dist = dist
            return 0
        next = self.queue.next
        while next != None:
            if next.v == w:
                next.dist = dist
                return 0
            next = next.next
        return 1

    def isEmpty(self):
        if self.empty or self.queue == None:
            return True
        return False

    def printList(self):
        lst = []
        lst.append((self.queue.v, self.queue.dist))
        self._printList(self.queue,lst)
    
    def _printList(self, node, lst):
        if node.next == None:
            print(lst)
            return
        lst.append((node.next.v, node.next.dist))
        self._printList(node.next,lst)

class DirectedEdge:
    # define edge between vertices v and w
    def __init__(self,v,w,weight):
        self.source = v
        self.to = w
        self.weight = weight
        self.string = f"Edge from {v} to {w} with weight {weight}"


class weightedDiGraph:

    def __init__(self):

        self.graph = defaultdict(list)
    
    def addEdge(self, v, w, weight):
        edge = DirectedEdge(v,w,weight)
        self.graph[v].append(edge)
    
    def adj(self, v):
        adj = []
        for w in self.graph[v]:
            adj.append(w)
        return adj

    def vertices(self):
        for e in self.graph:
            print(e)
            print(self.graph[e])
    
    def dijkstraSPFrom(self, s):
        q = PQ() # pq of vertices by distance from s
        distTo = []
        edgeTo= defaultdict(DirectedEdge) # mst vertices
        for v in range(len(self.graph)+1):
            distTo.append(float('inf'))
        distTo[s] = 0.0
        edgeTo[s] = None
        q.put(Node(s, 0.0))
        while q.isEmpty() == False:
            self.relax(q.remove(), distTo, edgeTo, q)
        return distTo

    def relax(self, s, distTo, edgeTo, q):
        v = s.v
        for e in self.adj(v):
            w = e.to
            if distTo[w] > distTo[v] + e.weight:
                distTo[w] = distTo[v] + e.weight
                edgeTo[w] = e
                if (q.contains(w)):
                     q.change(w, distTo[w])
                else:
                    q.put(Node(w, distTo[w]));

        

g = weightedDiGraph()
g.addEdge(0, 1, 0.5)
g.addEdge(0, 2, 0.8)
g.addEdge(1, 2, 0.4)
g.addEdge(2, 3, 0.9)
g.addEdge(3, 5, 1.2)
g.addEdge(1, 4, 2.2)
g.addEdge(4, 5, 3.0)

print(g.dijkstraSPFrom(0))


