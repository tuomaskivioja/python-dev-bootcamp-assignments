from collections import defaultdict

class PQ:
    def __init__(self, empty=True):
        self.queue = Edge
        self.empty = empty
    
    def put(self, edge):
        if self.isEmpty():
            self.queue = edge
            self.empty = False
            return
        if self.queue.weight > edge.weight:
            edge.next = self.queue
            self.queue = edge
            return
        next = self.queue.next
        curr = self.queue
        while next != None:
            if next.weight > edge.weight:
               break
            curr = next
            next = next.next
        edge.next = next
        curr.next = edge
    
    def remove(self):
        if self.queue == None:
            return None
        e = self.queue
        self.queue = self.queue.next
        return e

    def isEmpty(self):
        if self.empty or self.queue == None:
            return True
        return False

    def printList(self):
        lst = []
        lst.append((self.queue.one, self.queue.two, self.queue.weight))
        self._printList(self.queue,lst)
    
    def _printList(self, node, lst):
        if node.next == None:
            print(lst)
            return
        lst.append((node.next.one, node.next.two, node.next.weight))
        self._printList(node.next,lst)

class Edge:
    # define edge between vertices v and w
    def __init__(self,v,w,weight, next=None):
        self.one = v
        self.two = w
        self.weight = weight
        self.next = next
    
    def other(self, v):
        if v == self.one: 
            return self.two
        elif v == self.two:
            return self.one
        else:
            raise RuntimeError


class weightedGraph:

    def __init__(self):

        self.graph = defaultdict(list)
    
    def addEdge(self, v, w, weight):
        edge = Edge(v,w,weight)
        self.graph[v].append(edge)
        self.graph[w].append(edge)
    
    def adj(self, v):
        adj = []
        for w in self.graph[v]:
            adj.append(w)
        return adj

    def vertices(self):
        for e in self.graph:
            print(e)
            print(self.graph[e])

    def mstPrim(self):
        q = PQ() # crossing and ineligible edges
        mstE = [] # mst edges
        mstV = [] # mst vertices
        self.visit(0, q, mstV)
        while q.isEmpty() == False:
            minE = q.remove()
            print(minE.weight)
            v = minE.one
            w = minE.two
            if v in mstV and w in mstV:
                continue
            mstE.append(minE)
            if w in mstV:
                self.visit(v, q, mstV)
            if v in mstV:
                self.visit(w, q, mstV)
        return mstE

    def visit(self, s, q, mstV):
        mstV.append(s)
        for e in self.adj(s):
            if e.other(s) not in mstV:
                try:
                    print(q.queue.weight)
                except:
                    print(q.queue)
                q.put(e)

        

g = weightedGraph()
g.addEdge(0, 1, 0.5)
g.addEdge(0, 2, 0.8)
g.addEdge(1, 2, 0.4)
g.addEdge(2, 3, 0.9)
g.addEdge(3, 7, 1.2)
g.addEdge(4, 7, 3.0)

print(g.mstPrim())

#g.vertices()
    
# q = PQ()
# q.put(Edge(1,2,3))
# q.put(Edge(2,3,1))
# q.put(Edge(2,8,24))
# q.printList()