# 📚 Data Structures in Python

---

This repository contains my implementations of fundamental data structures written from scratch in Python.

The goal of this project is to deeply understand how common data structures work internally rather than relying on Python’s built-in abstractions. Each structure is implemented with explicit memory management logic, clear invariants, and well-defined behavior.

This repository will grow over time as more data structures and features are added.

---

# 📦 DynamicArrays (Class)

---

## 🔎 Overview

`DynamicArrays` is a manual implementation of a dynamic array (similar in behavior to Python’s built-in `list`).

Unlike Python lists, this implementation explicitly tracks:

- **capacity** → total allocated storage  
- **length** → number of elements currently stored  

The array automatically resizes itself when it becomes full or underutilized, ensuring efficient amortized performance.

---

## 🧠 Core Concepts

- Elements are stored in a fixed-size underlying list.
- When capacity is exceeded, the array **doubles in size**.
- When usage drops below one-quarter of capacity, the array **shrinks by half** (down to a minimum capacity).
- Index-based operations require manual element shifting.

---

## ⚙️ Class Interface (Methods)

---

### `__init__()`

Initializes the array with:

- `capacity = 4`
- `length = 0`
- An underlying list filled with `None`

---

### `__len__()`

Returns the current number of elements stored in the array.

---

### `__str__()`

Returns a readable string showing capacity, length, and array contents.
Useful for quick inspection of the array’s state.

---

#### `reset()`

**Reset the array to its initial state**

This method restores the array to its default values:  

- **capacity** is set back to `4`  
- **length** is reset to `0`  
- The underlying array is cleared and filled with `None`

It is useful for testing or reusing the same `DynamicArrays` object without creating a new instance.

**Time Complexity:** `O(n)`

---

### `access_element_by_index(index)`

Returns the element at the specified index if it is within bounds.  
Raises an `IndexError` otherwise.

**Time Complexity:** `O(1)`

---

### `resize(capacity)`

Creates a new underlying array with the given capacity and copies all existing elements into it.

- Does **not** modify `length`
- Used internally by other operations

**Time Complexity:** `O(n)`

---

### `_append(element)`

Adds an element to the end of the array.

- If the array is full → capacity doubles and elements are copied
- Otherwise → element is inserted directly

**Time Complexity:**
- Amortized → `O(1)`
- Worst case → `O(n)` (during resizing)

---

### `_pop()`

Removes the last element in the array.

- If usage drops below one-quarter of capacity → array shrinks
- Raises an error if the array is empty

**Time Complexity:**
- Amortized → `O(1)`
- Worst case → `O(n)` (during resizing)

---

### `insert_at_index(index, element)`

Inserts an element at a specific index.

- Elements are shifted to the right
- Resizes if necessary

**Time Complexity:** `O(n)`

---

### `remove_at_index(index)`

Removes the element at a specific index.

- Elements are shifted to the left
- Shrinks if underutilized

**Time Complexity:** `O(n)`

---

# 🚀 Future Work

---

Planned additions include:

- Additional data structures (Stacks, Queues, Linked Lists, Trees)
- Unit tests
- Performance benchmarks
- Visualization helpers

This README will continue evolving as the project grows.

---

# 🧪 problems.py - For DynamicArrays (class)

---

A dedicated `problems` file is included to manually test and demonstrate the behavior of the `DynamicArrays` class.

This file is designed to:

- Showcase internal resizing behavior
- Validate shifting logic during insertions and removals
- Demonstrate shrinking when underutilized
- Test edge cases safely using `try/except`
- Provide clear console output for step-by-step verification

---

## 🔹 What This File Covers

#### 1. Setup
- Instantiates a new `DynamicArrays` object
- Prints the initial state

#### 2. Basic Append / Pop
- Appends multiple elements to trigger growth
- Pops elements to trigger shrink behavior
- Verifies amortized resizing logic

#### 3. Access by Index
- Confirms correct element retrieval
- Validates bounds checking

#### 4. Insert at Index
- Tests element shifting to the right
- Verifies resizing when capacity is exceeded

#### 5. Remove at Index
- Tests element shifting to the left
- Ensures proper cleanup of unused slots

#### 6. Resize Behaviour
- Forces growth and shrink conditions
- Confirms minimum capacity protection

#### 7. Edge Cases
- Accessing an empty array
- Popping from an empty array
- Inserting at index `0`
- Inserting at the end
- Removing first and last elements
- Repeated removals to trigger shrinking
- Preventing shrink below minimum capacity

All edge cases are handled using `try/except` so the program continues running.

---

### 🎯 Purpose

The goal of this file is not automated testing, but **educational verification**.  

It allows observation of:

- Internal state transitions
- Capacity vs length changes
- Shifting behavior
- Shrink thresholds
- Error handling

As the project grows, this section may evolve into formal unit tests.

---

# 📦 bfs_dfs (Class)

---

# 📦 graph (Class)

---

# 📦 problems.py - For bfs_dfs (class) and graph (class)

---

# 📦 hash_table (Class)

---

# 📦 problems.py - For hash_table (Class)

---

# 📦 doubly_linked_list (Class)

---

# 📦 singly_linked_list (Class)

---

# 📦 problems.py - For doubly_linked_list (Class) and singly_linked_list (Class)

---

# 📦 Queue (Class)

---

## Overview

`Queue` is a First-In, First-Out (FIFO) data structure built on top of the custom `DynamicArrays` implementation.

Unlike Python’s built-in queue structures, this implementation explicitly separates:

- **Storage responsibility** → handled by `DynamicArrays`
- **Behavior responsibility** → handled by `Queue`

Elements are added to the **back** and removed from the **front**, preserving FIFO order.

---

### Core Concepts

- Built using **composition** (Queue *has a* DynamicArray)
- Enqueue inserts at the back
- Dequeue removes from the front
- Automatically benefits from DynamicArray resizing
- Shifting during dequeue results in **O(n)** removal

---

### Class Interface

---

#### `__init__`

Initializes an empty queue by creating a new `DynamicArrays` instance for internal storage.

---

#### `__len__`

Returns the number of elements currently stored in the queue.

Time complexity: **O(1)**

---

#### `__str__`

Returns a readable string representation of the queue contents.

---

#### `enqueue(value)`

Adds a value to the back of the queue.

If the underlying array is full, resizing is handled automatically by `DynamicArrays`.

Time complexity:  
- **Amortized O(1)**  
- Worst-case **O(n)** during resizing

---

#### `dequeue()`

Removes and returns the value at the front of the queue.

Raises `IndexError` if the queue is empty.

Time complexity: **O(n)** (due to element shifting)

---

#### `peek()`

Returns the value at the front without removing it.

Raises `IndexError` if the queue is empty.

Time complexity: **O(1)**

---

#### `is_empty()`

Returns `True` if the queue contains no elements.

Time complexity: **O(1)**

---

#### `reset()`

**Reset the array to its initial state**

Refer to `DynamicArrays (Class) - reset()`

Time complexity: **O(1)**

---

### Design Notes

- Queue does not manage memory or resizing directly.
- All storage mechanics are delegated to `DynamicArrays`.
- This separation maintains clean abstraction and modularity.
- The implementation prioritizes clarity over optimal dequeue performance.

---

### Future Improvements

- Implement a circular queue for true **O(1)** dequeue
- Add benchmarking comparisons
- Add unit tests
- Integrate into BFS implementation

---

# 🧪 problems.py - For queue (class)

---

## Overview

This file contains structured test cases for validating the `Queue` implementation.

The goal is to verify:

- FIFO behaviour
- Correct length tracking
- Proper handling of empty states
- Correct resizing behaviour
- Stability under mixed operations

Each section prints the queue state after operations to visually confirm correctness.

---

### 1. Setup & Initialization

Creates a new `Queue` instance and verifies:

- Initial state is empty
- Length is `0`
- `is_empty()` returns `True`

---

### 2. Basic Enqueue Test

Performs 5 enqueue operations and verifies:

- Elements are added to the back
- Order is preserved
- Length increases correctly
- `is_empty()` returns `False`

---

### 3. Peek Test

Confirms that:

- `peek()` returns the front element
- The queue remains unchanged after peeking
- Length does not change

---

### 4. Multiple Dequeue Test

Performs 5 dequeue operations and verifies:

- Elements are removed in FIFO order
- Removed values are printed
- Length decreases correctly
- Queue eventually becomes empty

---

### 5. Enqueue After Dequeue

Tests queue stability after being emptied by:

- Performing additional enqueue operations
- Confirming order is preserved
- Confirming length updates correctly

---

### 6. Empty Queue Edge Cases

Validates proper error handling by:

- Attempting `dequeue()` on an empty queue
- Attempting `peek()` on an empty queue
- Catching and printing `IndexError` without crashing the program

---

### 7. Resizing Behaviour Stress Test

Performs 33 enqueue operations to:

- Trigger underlying dynamic resizing
- Confirm no data corruption
- Confirm length accuracy after large insertions

---

### 8. Mixed Operation Test

Simulates realistic usage by mixing:

- Enqueue
- Dequeue
- Peek

This confirms:

- FIFO behaviour remains consistent
- Length tracking remains accurate
- No internal corruption occurs during alternating operations

---

### Design Notes

- All output is printed explicitly to visualize behaviour.
- Exceptions are caught using `try/except` to prevent program termination.
- The test file does not access internal storage directly, preserving abstraction.

---

# 📦 binary_search (Class)

---

# 📦 linear_search (Class)

---

# 📦 bubble_sort (Class)

---

# 📦 counting_sort (Class)

---

# 📦 insertion_sort (Class)

---

# 📦 merge_sort (Class)

---

# 📦 quick_sort (Class)

---

# 📦 radix_sort (Class)

---

# 📦 selection_sort (Class)

---

# 📦 stack (Class)

---

# 📦 problems.py - For stack (Class)

---

# 📦 test_all (Class)

---

# 📦 avl_tree (Class)

---

# 📦 binary_tree (Class)

---

# 📦 bst (Class)

---

# 📦 traversals (Class)

---












