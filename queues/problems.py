# Queue Practice Problems
from queue import Queue

# Setup & Initialization
print("\n# Setup & Initialization")
my_queue = Queue()
print(my_queue)
print(f"Length of my_queue: {len(my_queue)}")
print(f"my_queue is empty: {my_queue.is_empty()}")

# Basic Enqueue Test
print("\n# Basic Enqueue Test")
print("5 enqueues on my_queue: ")
print(f"{my_queue}")
print(f"Length of my_queue: {len(my_queue)}")
print(f"my_queue is empty: {my_queue.is_empty()}")

for item in range(1, 6):
    my_queue.enqueue(item)
    print(f"\n{my_queue}")
    print(f"Length of my_queue: {len(my_queue)}")
    print(f"my_queue is empty: {my_queue.is_empty()}")

# Peek Test
print("\n# Peek Test")
print(f"my_queue before peek: {my_queue}")
print(f"Peek on my_queue: {my_queue.peek()}")
print(f"my_queue after peek: {my_queue}")

# Multiple Dequeue Test
print("\n# Multiple Dequeue Test")
print("5 dequeues on my_queue: ")
print(f"{my_queue}")
print(f"Length of my_queue: {len(my_queue)}")
print(f"my_queue is empty: {my_queue.is_empty()}")

for item in range(1, 6):
    removed = my_queue.dequeue()
    print(f"\n{my_queue}")
    print(f"Length of my_queue: {len(my_queue)}")
    print(f"my_queue is empty: {my_queue.is_empty()}")
    print(f"Removed: {removed}")

# Enqueue After Dequeue
print("\n# Enqueue After Dequeue")
print("my_queue after 5 enqueues: ")
print(f"{my_queue}")
print(f"Length of my_queue: {len(my_queue)}")
print(f"my_queue is empty: {my_queue.is_empty()}")

for item in range(1, 6):
    my_queue.enqueue(item * 100)
    print(f"\n{my_queue}")
    print(f"Length of my_queue: {len(my_queue)}")
    print(f"my_queue is empty: {my_queue.is_empty()}")

# Empty Queue Edge Case
print("\n# Dequeue on empty queue")
my_queue.reset()
print(f"my_queue: {my_queue}")
try:
    print("dequeue")
    my_queue.dequeue()
except IndexError as e:
    print(f"Error: {e}")
print("\n# Peek on empty queue")
print(f"my_queue: {my_queue}")

try:
    print("peek")
    my_queue.peek()
except IndexError as e:
    print(f"Error: {e}")

# Resizing Behavior Stress Test
print("\n# Resizing Behavior Stress Test")
print("Perform 33 enqueues on queue: ")
for item in range(1, 34):
    my_queue.enqueue(item * 10)
print(f"my_queue: {my_queue}")
print(f"my_queue length: {len(my_queue)}")

# Mixed Operation Test
print("\n# Mixed Operation Test")
my_queue.reset()
print(my_queue)

print("\nenqueue 1")
my_queue.enqueue(1)
print(my_queue)
print(f"Length: {len(my_queue)}")

print("\nenqueue 2")
my_queue.enqueue(2)
print(my_queue)
print(f"Length: {len(my_queue)}")

print("\ndequeue")
removed = my_queue.dequeue()
print(my_queue)
print(f"Length: {len(my_queue)}")
print(f"Removed: {removed}")

print("\nenqueue 3")
my_queue.enqueue(3)
print(my_queue)
print(f"Length: {len(my_queue)}")

print("\nenqueue 4")
my_queue.enqueue(4)
print(my_queue)
print(f"Length: {len(my_queue)}")

print("\ndequeue")
removed = my_queue.dequeue()
print(my_queue)
print(f"Length: {len(my_queue)}")
print(f"Removed: {removed}")

print("\npeek")
print(f"Peeked: {my_queue.peek()}")
print(my_queue)
print(f"Length: {len(my_queue)}")

print("\nenqueue 5")
my_queue.enqueue(5)
print(my_queue)
print(f"Length: {len(my_queue)}")
