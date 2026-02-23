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

# 📂 Graph.py

## Graph – Undirected Adjacency List Implementation

This module implements an undirected graph using an adjacency list representation.

Each vertex is stored as a key in a dictionary, and its value is a list of connected vertices (neighbours).

Graph structure:

self.adj_list = {
    vertex: [neighbour1, neighbour2, ...]
}

This design allows efficient vertex lookup and flexible edge management.

## Design Overview

Graph is undirected

No duplicate vertices allowed

No duplicate edges allowed

Uses a Python dictionary for adjacency storage

Neighbours are stored in lists

## Constructor

Graph()

Initializes an empty graph.

graph = Graph()

Creates:

self.adj_list = {}

Time Complexity: O(1)

## String Representation

str()

Returns a readable string representation of the graph.

Each line shows:

vertex: [neighbour1, neighbour2, ...]

Example:

A: ['B', 'C']
B: ['A']
C: ['A']

Time Complexity: O(V)

## add_vertex(vertex)

Adds a new vertex to the graph.

If the vertex does not exist → it is added.

If the vertex already exists → duplicates are not allowed.

Example:

graph.add_vertex("A")

Time Complexity: O(1)

## add_edge(v1, v2)

Adds an undirected edge between two vertices.

Requirements:

Both vertices must already exist.

Duplicate edges are prevented.

Example:

graph.add_edge("A", "B")

Internally:

Adds v2 to v1's neighbour list

Adds v1 to v2's neighbour list

Time Complexity: O(1) average

## remove_edge(v1, v2)

Removes an undirected edge between two vertices.

Raises:

ValueError if either vertex does not exist

ValueError if the edge does not exist

Example:

graph.remove_edge("A", "B")

Time Complexity: O(V) worst case
(Because list removal requires searching)

## remove_vertex(vertex)

Removes a vertex and all connected edges.

Steps:

Remove the vertex from all neighbour lists

Delete the vertex from the adjacency list

Example:

graph.remove_vertex("A")

Time Complexity: O(V + E)
(Because connected edges must be removed)

## Time & Space Complexity Summary

Space Complexity:

O(V + E)

V = number of vertices

E = number of edges

Time Complexity Summary:

add_vertex → O(1)

add_edge → O(1) average

remove_edge → O(V)

remove_vertex → O(V + E)

str → O(V)

## Key Characteristics

Undirected graph

Adjacency list representation

Prevents duplicate vertices

Prevents duplicate edges

Safe edge removal

Compatible with BFS and DFS traversal modules

---

# 📂 bfs_dfs.py

## 🟦 Breadth-First Search (BFS)

Uses the custom Queue class to explore the graph level-by-level.

Starts at the given vertex

Visits all immediate neighbors first

Continues outward until all reachable vertices are processed

Marks vertices as visited when enqueued to prevent duplicates

Time Complexity: O(V + E)

(---)

## 🟥 Depth-First Search (DFS)

Uses the custom Stack class to explore the graph as deeply as possible before backtracking.

Starts at the given vertex

Follows one path fully before exploring alternatives

Uses a visited set to prevent revisiting vertices

Returns traversal order

Time Complexity: O(V + E)

---

# 📦 problems.py - For bfs_dfs and graph (class)

## 🧪 Graph – Practice & Validation

This problems file validates the correctness and robustness of the Graph implementation using structured tests.

### ✔ Covered Scenarios

Graph initialization

Adding vertices

Adding undirected edges

Preventing duplicate edges

Handling invalid edge insertions

Removing edges

Removing vertices

Safe vertex deletion while iterating

Edge and vertex error handling

Full graph teardown (removing all vertices)

### 🔍 What This Confirms

The adjacency list remains symmetric for undirected edges

Edge removal updates both vertices correctly

Vertex removal clears all connected references

Dictionary mutation is handled safely during iteration

Errors are raised properly for invalid operations

This file ensures the graph behaves correctly under normal usage, edge cases, and structural stress testing.

## BFS & DFS Practice Problems

### Overview
This problems file validates the Breadth-First Search (BFS) and Depth-First Search (DFS) implementations using the custom Graph, Queue, and Stack classes.

It ensures:

Correct traversal order

No duplicate visits

Proper cycle handling

Safe error handling

Correct behavior on disconnected graphs

### Graph Setup

A connected graph is constructed with:

Multiple branching paths

A large cycle

A mix of shallow and deep traversal paths

This allows clear comparison between BFS (level-order traversal) and DFS (depth-first traversal).

### Tests Included

BFS traversal from different start nodes

DFS traversal from different start nodes

Invalid start vertex handling

Disconnected vertex behavior

Dedicated cycle-only graph validation

### What This Confirms

Visited tracking prevents infinite loops

Traversal structures (Queue for BFS, Stack for DFS) behave correctly

No duplicate vertices appear in results

Traversals terminate safely in cyclic graphs

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

# 🧱 Stack

---

## Overview

`Stack` is a Last-In, First-Out (LIFO) data structure built on top of the custom `DynamicArrays` implementation.

Unlike a queue, which removes elements from the front, a stack removes elements from the top (the most recently added item).

This implementation delegates storage and resizing responsibilities to `DynamicArrays` while defining stack-specific behavior.

---

### Core Concepts

- Built using **composition** (Stack *has a* DynamicArray)
- Push inserts at the top (end of array)
- Pop removes from the top (end of array)
- No element shifting required
- Benefits from automatic resizing in `DynamicArrays`

---

### Class Interface

---

#### `__init__`

Initializes an empty stack by creating a new `DynamicArrays` instance for internal storage.

---

#### `__len__`

Returns the number of elements currently stored in the stack.

Time complexity: **O(1)**

---

#### `__str__`

Returns a readable string representation of the stack contents.

Only active elements are displayed.

---

#### `push(value)`

Adds a value to the top of the stack.

Time complexity:  
- **Amortized O(1)**  
- Worst-case **O(n)** during resizing

---

#### `pop()`

Removes and returns the value at the top of the stack.

Raises `IndexError` if the stack is empty.

Time complexity:  
- **Amortized O(1)**

---

#### `peek()`

Returns the value at the top without removing it.

Raises `IndexError` if the stack is empty.

Time complexity: **O(1)**

---

#### `is_empty()`

Returns `True` if the stack contains no elements.

Time complexity: **O(1)**

---

#### `reset()`

**Reset the array to its initial state**

Refer to `DynamicArrays (Class) - reset()`

Time complexity: **O(1)**

---

### Design Notes

- Stack does not manage memory or resizing directly.
- All storage mechanics are delegated to `DynamicArrays`.
- Unlike Queue, Stack operations do not require element shifting.
- This makes stack removal operations more efficient than queue removal in this implementation.

---

### Future Improvements

- Add benchmarking comparisons
- Implement stack using a linked list
- Use Stack in DFS traversal
- Add unit tests

---

# 🧪 problems.py - For stack (Class)

This file validates the correctness and robustness of the `Stack` implementation through structured tests.

## What Is Tested

- ✅ Initialization and empty state
- ✅ Basic `push()` operations
- ✅ `peek()` returning the top element without removal
- ✅ Multiple `pop()` operations (verifying LIFO behaviour)
- ✅ Correct length tracking after each operation
- ✅ Error handling for `pop()` and `peek()` on an empty stack
- ✅ Dynamic resizing under heavy push operations
- ✅ Mixed operation sequences (push → pop → peek → push)

### Key Validation Goals

- Stack follows **Last-In, First-Out (LIFO)** order  
- No element shifting occurs (operations occur at the end)  
- Length and state remain consistent  
- No corruption during resizing or resets  

This practice file ensures the stack behaves correctly under normal, edge-case, and stress scenarios.

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












