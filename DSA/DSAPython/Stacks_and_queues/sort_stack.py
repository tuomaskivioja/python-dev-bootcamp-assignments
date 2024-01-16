from stack import Stack
from queue import Queue


def reverse_string(s):
    stack = Stack()
    for char in s:
        stack.push(char)

    reversed_string = ''
    while len(stack.items) > 0:
        reversed_string += stack.pop()

    return reversed_string


# Example usage
print(reverse_string("hello"))  # Output: "olleh"


def sort_stack(original_stack):
    temp_stack = Stack()
    while len(original_stack.items) > 0:
        temp = original_stack.pop()
        while len(temp_stack.items) > 0 and temp_stack.peek() > temp:
            original_stack.push(temp_stack.pop())
        temp_stack.push(temp)

    while len(temp_stack.items) > 0:
        original_stack.push(temp_stack.pop())

    return original_stack


# Example usage
stack = Stack()
for i in [34, 3, 31, 98, 92, 23]:
    stack.push(i)
sorted_stack = sort_stack(stack)
print(sorted_stack.items)  # Output: [98, 92, 34, 31, 23, 3]


class QueueUsingStacks:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def enqueue(self, item):
        self.in_stack.push(item)

    def dequeue(self):
        if len(self.out_stack.items) == 0:
            while len(self.in_stack.items) > 0:
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.pop() if len(self.out_stack.items) > 0 else None


# Example usage
queue = QueueUsingStacks()
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())  # Output: 1
queue.enqueue(3)
print(queue.dequeue())  # Output: 2



def is_palindrome_queue(queue):
    stack = Stack()
    original_queue = list(queue.items)

    while len(queue.items) > 0:
        stack.push(queue.dequeue())

    while len(stack.items) > 0:
        if stack.pop() != original_queue.pop(0):
            return False

    return True


# Example usage
q = Queue()
for i in [1, 2, 3, 2, 1]:
    q.enqueue(i)
print(is_palindrome_queue(q))  # Output: True

q = Queue()
for i in [1, 2, 3, 4, 5]:
    q.enqueue(i)
print(is_palindrome_queue(q))  # Output: False
