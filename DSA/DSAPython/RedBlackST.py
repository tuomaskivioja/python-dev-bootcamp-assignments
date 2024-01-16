
RED = True
BLACK = False
class Node:
    def __init__(self, key, val):
        self.value = val
        self.key = key
        self.right = None
        self.left = None
        self.color = RED

class RedBlackST:

    def __init__(self):
        self.root = None
        self.root.color = BLACK

    def rotateLeft(self, n):
        r = n.right
        n.right = r.left
        r.left = n
        r.color = n.color
        n.color = RED
        return r
    
    def rotateRight(self, n):
        l = n.left
        n.left = l.right
        l.right = n
        l.color = n.color
        n.color = RED
        return l

    def flipColors(n):
        n.color = RED
        n.left.color = BLACK
        n.right.color = BLACK

    def isRed(n):
        if n == None:
            return False
        return n.color

    def put(self, key, val):
        self.root = self._put(self.root, key, val)

    def _put(self, n, key, val):
        if n == None:
            return Node(key, val)
        if key < n.key:
            n.left = self._put(n.left, key, val)
        elif key > n.key:
            n.right = self._put(n.right, key, val)
        else:
            n.value = val
        if self.isRed(n.right) == True and self.isRed(n.left) == False:
            n = self.rotateLeft(n)
        if self.isRed(n.left) and self.isRed(n.left.left):
            n = self.rotateRight(n)
        if self.isRed(n.left) and self.isRed(n.right):
            self.flipColors(n) 

        return n