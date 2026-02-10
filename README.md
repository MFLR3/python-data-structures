# Data Structures in Python

This repository contains my implementations of fundamental data structures written from scratch in Python.

The goal of this project is to deeply understand how common data structures work internally rather than relying on Python’s built-in abstractions. Each structure is implemented with explicit memory management logic, clear invariants, and well-defined behavior.

This repository will grow over time as more data structures and features are added.

---

## DynamicArrays

### Overview

`DynamicArrays` is a manual implementation of a dynamic array (similar in behavior to Python’s built-in `list`).  
Unlike Python lists, this implementation explicitly tracks:

- **capacity**: the total allocated storage
- **length**: the number of elements currently stored

The array automatically resizes itself when it becomes full or underutilized, ensuring efficient amortized performance.

---

### Core Concepts

- Elements are stored in a fixed-size underlying list.
- When capacity is exceeded, the array **doubles in size**.
- When usage drops below one-quarter of capacity, the array **shrinks by half** (down to a minimum capacity).
- Index-based operations require manual element shifting.

---

### Class Interface

#### `__init__`
Initializes the array with:
- capacity = 4
- length = 0
- an underlying list filled with `None`

---

#### `__len__`
Returns the current number of elements stored in the array.

---

#### `access_element_by_index(index)`
Returns the element at the specified index if it is within bounds.  
Raises an `IndexError` otherwise.

Time complexity: **O(1)**

---

#### `resize(capacity)`
Creates a new underlying array with the given capacity and copies all existing elements into it.

This method does not modify `length` and is used internally by other operations.

Time complexity: **O(n)**

---

#### `_append(element)`
Adds an element to the end of the array.

- If the array is full, capacity is doubled and elements are copied into a new array.
- Otherwise, the element is added directly.

Time complexity:
- **Amortized O(1)**
- Worst-case **O(n)** during resizing

---

#### `_pop()`
Removes the last element in the array.

- If usage drops below one-quarter of capacity, the array shrinks.
- Raises an error if the array is empty.

Time complexity:
- **Amortized O(1)**
- Worst-case **O(n)** during resizing

---

#### `insert_at_index(index, element)`
Inserts an element at a specific index.

- Elements are shifted to the right.
- The array resizes if necessary.

Time complexity: **O(n)**

---

#### `remove_at_index(index)`
Removes the element at a specific index.

- Elements are shifted to the left.
- The array shrinks if underutilized.

Time complexity: **O(n)**

---

## Future Work

This README will be expanded as the project grows.
