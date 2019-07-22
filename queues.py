#FIFO
"""
import Queue


q = Queue.Queue()
for item in range(5):
    q.put(item)

while not q.empty():
    print q.get()

#LIFO

q = Queue.LifoQueue()
for item in range(5):
    q.put(item)

while not q.empty():
    print q.get()

"""

#deque(collections)
import collections

deque = collections.deque([1,2,3])

deque.append(4)

print("after appending at right is:")
print(deque)

deque.appendleft(6)

print ("after appending at left is:")
print(deque)

deque.pop()

print("after deleting from right is:")
print(deque)

deque.popleft()

print("after deleting from left is:")
print(deque)
