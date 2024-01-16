
class Bag:
    def __init__(self, key=None, val=None):
        self.value = val
        self.key = key
        self.next = None
    
    def insert(self, key, val):
        node = Bag(key, val)
        if self.next == None:
            self.next = node
        else:
            self._insert(self.next, node, key, val)
    
    def _insert(self, curr, node, key, val):
        if curr.next == None:
            curr.next = node
        else:
            self._insert(curr.next, key, val)
            
    def insertAfterIndex(self, key, val, index: int):
        node = Bag(key, val)
        i = 0
        curr = self
        while i != index:
            curr = curr.next
            i += 1
        temp = curr.next
        curr.next = node
        node.next = temp
    
    def printList(self):
        lst = []
        lst.append((self.key, self.value))
        self._printList(self,lst)

    def _printList(self, node, lst):
        if node.next == None:
            print(lst)
            return
        lst.append((node.next.key, node.next.value))
        self._printList(node.next,lst)