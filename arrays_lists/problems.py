# DynamicArrays Practice Problems
from dynamic_arrays import DynamicArrays

# 1. SETUP
print("# 1. SETUP")
arr = DynamicArrays()
arr.__init__()
print(f"{arr}\n")

# 2. BASIC APPEND/POP
print("# 2. BASIC APPEND/POP")
print("After 31 appends: ")
for item in range(0, 31):
    arr.append(item)
print(f"{arr}\n")
for item in range(0, 29):
    arr.pop()
print("After 29 pops: ")
print(f"{arr}\n")

# 3. ACCESS BY INDEX
print("# 3. ACCESS BY INDEX")
element = arr.access_element_by_index(1)
print(f"Element at index 1: {element}\n")

# 4. INSERT AT INDEX
print("# 4. INSERT AT INDEX")

arr.insert_at_index(2, "Inserted at index 2")
arr.insert_at_index(3, "Inserted at index 3")
arr.insert_at_index(4, "Inserted at index 4")
print(f"{arr}\n")

# 5. REMOVE AT INDEX
print("# 5. REMOVE AT INDEX")
arr.remove_at_index(2)
print("Removed at index 2: ")
print(f"{arr}\n")

# 6. RESIZE BEHAVIOUR
print("# 6. RESIZE BEHAVIOUR")
arr.reset()
print("Array after reset: ")
print(f"{arr}\n")
for item in range(0, 4):
    arr.append(item)
print("Array at full capacity: ")
print(f"{arr}\n")
print("Full Array after 1 append: ")
arr.append("This appended element has triggered the resize method")
print(f"{arr}\n")
print("Array after 3 pops: ")
for item in range(0, 3):
    arr.pop()
print(f"{arr}\n")

# 7. EDGE CASES
print("# 7. EDGE CASES")
arr.reset()
# Accessing an empty array > raises IndexError.
try:
    element = arr.access_element_by_index(0)
except IndexError as e:
    print(f"Error: {e}")

# Popping from an empty array > raises IndexError.
try:
    element = arr.pop()
except IndexError as e:
    print(f"Error: {e}\n")

# Inserting at index 0 or at the end > ensures proper shifting without errors.
print("# Inserting at index 0 or at the end > ensures proper shifting without errors.")
print("Before insert at index 0:")
print(f"{arr}\n")
arr.insert_at_index(0, "Inserted at 0.")
print("After insert at index 0:")
print(f"{arr}\n")

print("# Inserting at index 3 or at the end > ensures proper shifting without errors.")
for item in range(1, 4):
    arr.append(item)
print("Before insert at index 3:")
print(f"{arr}\n")
arr.insert_at_index(3, "Inserted at 3.")
print("After insert at index 3:")
print(f"{arr}\n")

# Removing the first or last element > shrinking logic triggers if needed.
print("# Removing the first or last element > shrinking logic triggers if needed.")
arr.reset()
for item in range(0, 8):
    arr.append(item)
print("Before removing last item: ")
print(arr)
arr.remove_at_index(7)
print("After removing last item: ")
print(arr)
arr.remove_at_index(0)
print("After removing first item: ")
print(arr)
print("\nKeep removing 1st item until shrink triggered: ")
while arr.length > 0:
    print(arr)
    print(f"Remove {arr.access_element_by_index(0)}")
    arr.remove_at_index(0)
    print(f"{arr}\n")
    if arr.capacity == 4:
        print("Shrink achieved. \n")
        break

# Shrinking below minimum capacity > should stop shrinking at capacity = 4.
print("# Shrinking below minimum capacity > should stop shrinking at capacity = 4. ")
while arr.length > 0:
    print(arr)
    print("Pop item: ")
    arr.pop()
    print(f"{arr} \n")
