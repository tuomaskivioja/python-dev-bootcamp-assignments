from queue import Queue


def hot_potato(names: list, num: int) -> str:
   queue = Queue(names)

   while len(queue.items) > 1:
      for i in range(num - 1):
         queue.enqueue(queue.dequeue())
      print("removing", queue.peek())
      queue.dequeue()

   return queue.peek()


# Testing the function
names = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
num = 3
print(hot_potato(names, num))  # Output: "Bill"