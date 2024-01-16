

class Node:
    def __init__(self, key, val):
        self.value = val
        self.key = key
        self.right = None
        self.left = None

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def min(self):
        return min(self.root)
    
    def _min(self, n):
        if n.left == None:
            return n
        return self._min(n.left)

    def _deleteMin(self, x):
        if x.left == None:
            return x.right
        x.left = self._deleteMin(x.left)
        return x

    def put(self, x):
        if self.root == None or self.root.key == x.key:
            self.root = x
            return
        if x.key > self.root.key:
            if self.root.right == None:
                self.root.right = x
                return
            self._put(x, self.root.right)
        elif x.key < self.root.key:
            if self.root.left == None:
                self.root.left = x
                return
            self._put(x, self.root.left)

    def _put(self, x, n):
        if x.key == n.key:
            n.value = x.value
        elif x.key > n.key:
            if n.right == None:
                n.right = x
                return
            self._put(x, n.right)
        elif x.key < n.key:
            if n.left == None:
                n.left = x
                return
            self._put(x, n.left)

    def get(self, key):
        if self.root.key == key:
            return self.root.value
        elif key > self.root.key:
            if self.root.right == None:
                return None
            return self._get(key, self.root.right)
        elif key < self.root.key:
            if self.root.left == None:
                return None
            return self._get(key, self.root.left)

    def _get(self, key, n):
        if n.key == key:
            return n.value
        elif key > n.key:
            if n.right == None:
                return None
            return self._get(key, n.right)
        elif key < n.key:
            if n.left == None:
                return None
            return self._get(key, n.left)        

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, n, key):
        if n == None:
            return None
        if n.key == key:
            if n.right == None:
                return n.left
            elif n.left == None:
                return n.right
            minNode = min(n.right)
            minNode.right = self._deleteMin(n.right)
            minNode.left = n.left
            return minNode
        
        if key < n.key:
            n.left = self._delete(n.left, key)
        elif key > n.key:
            n.right = self._delete(n.right, key)
        return n



bst = BinarySearchTree()

bst.put(Node('a', 3))
bst.put(Node('b', 2))
bst.put(Node('c', 5))
bst.put(Node('d', 1))
bst.put(Node('b', 10))
bst.put(Node('e', 4))

#print(bst.size())
#print(bst.root.value)
#print(bst.root.right.value)
print(bst.get('a'))
print(bst.get('b'))
print(bst.get('c'))
print(bst.get('d'))
print(bst.get('e'))
print("LET'S DELETE")
#bst.delete('a')
#bst.delete('b')
bst.delete('c')
#bst.delete('d')
print(bst.get('a'))
print(bst.get('b'))
print(bst.get('c'))
print(bst.get('d'))
print(bst.get('e'))
