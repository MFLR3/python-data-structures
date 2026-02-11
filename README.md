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

# 🧪 problems.py

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