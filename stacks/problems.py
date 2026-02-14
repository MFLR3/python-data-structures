# Stack Practice Problems
from stack import Stack

# Setup & Initialization
print("\n# Setup & Initialization")
my_stack = Stack()
print(my_stack)
print(f"Length of my_stack: {len(my_stack)}")
print(f"my_stack is empty: {my_stack.is_empty()}")

# Basic Push Test
print("\n# Basic Push Test")
print("5 pushes on my_stack: ")
print(f"{my_stack}")
print(f"Length of my_stack: {len(my_stack)}")
print(f"my_stack is empty: {my_stack.is_empty()}")

for item in range(1, 6):
    my_stack.push(item)
    print(f"\n{my_stack}")
    print(f"Length of my_stack: {len(my_stack)}")
    print(f"my_stack is empty: {my_stack.is_empty()}")

# Peek Test
print("\n# Peek Test")
print(f"my_stack before peek: {my_stack}")
print(f"Peek on my_stack: {my_stack.peek()}")
print(f"my_stack after peek: {my_stack}")

# Multiple Pop Test
print("\n# Multiple Pop Test")
print("5 pops on my_stack: ")
print(f"{my_stack}")
print(f"Length of my_stack: {len(my_stack)}")
print(f"my_stack is empty: {my_stack.is_empty()}")

for item in range(1, 6):
    removed = my_stack.pop()
    print(f"\n{my_stack}")
    print(f"Length of my_stack: {len(my_stack)}")
    print(f"my_stack is empty: {my_stack.is_empty()}")
    print(f"Removed: {removed}")

# Push After Pop
print("\n# Push After Pop")
print("my_stack after 5 pops: ")
print(f"{my_stack}")
print(f"Length of my_stack: {len(my_stack)}")
print(f"my_stack is empty: {my_stack.is_empty()}")

for item in range(1, 6):
    my_stack.push(item * 100)
    print(f"\n{my_stack}")
    print(f"Length of my_stack: {len(my_stack)}")
    print(f"my_stack is empty: {my_stack.is_empty()}")

# Empty Stack Edge Case
print("\n# Pop on empty Stack")
my_stack.reset()
print(f"my_stack: {my_stack}")
try:
    print("pop")
    my_stack.pop()
except IndexError as e:
    print(f"Error: {e}")
print("\n# Peek on empty stack")
print(f"my_stack: {my_stack}")

try:
    print("peek")
    my_stack.peek()
except IndexError as e:
    print(f"Error: {e}")

# Resizing Behavior Stress Test
print("\n# Resizing Behavior Stress Test")
print("Perform 33 pushes on stack: ")
for item in range(1, 34):
    my_stack.push(item * 10)
print(f"my_stack: {my_stack}")
print(f"my_stack length: {len(my_stack)}")

# Mixed Operation Test
print("\n# Mixed Operation Test")
my_stack.reset()
print(my_stack)

print("\npush 1")
my_stack.push(1)
print(my_stack)
print(f"Length: {len(my_stack)}")

print("\npush 2")
my_stack.push(2)
print(my_stack)
print(f"Length: {len(my_stack)}")

print("\npop")
removed = my_stack.pop()
print(my_stack)
print(f"Length: {len(my_stack)}")
print(f"Removed: {removed}")

print("\npush 3")
my_stack.push(3)
print(my_stack)
print(f"Length: {len(my_stack)}")

print("\npush 4")
my_stack.push(4)
print(my_stack)
print(f"Length: {len(my_stack)}")

print("\npop")
removed = my_stack.pop()
print(my_stack)
print(f"Length: {len(my_stack)}")
print(f"Removed: {removed}")

print("\npeek")
print(f"Peeked: {my_stack.peek()}")
print(my_stack)
print(f"Length: {len(my_stack)}")

print("\npush 5")
my_stack.push(5)
print(my_stack)
print(f"Length: {len(my_stack)}")
