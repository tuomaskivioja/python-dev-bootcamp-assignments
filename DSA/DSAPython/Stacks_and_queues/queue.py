from collections import deque


class Queue:
    def __init__(self, items=None):
        if items is None:
            items = []
        self.items = deque(items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) > 0:
            return self.items.popleft()

    def peek(self):
        if len(self.items) > 0:
            return self.items[0]
