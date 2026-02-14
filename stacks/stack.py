# stack
import arrays_lists.dynamic_arrays as da


class Stack:
    # Initialize an empty stack using DynamicArrays for storage
    def __init__(self):
        self.data = da.DynamicArrays()

    # Return the number of elements currently in the stack
    def __len__(self):
        return len(self.data)

    # Return a readable string representation of the stack
    # Only active elements are displayed (no None padding)
    def __str__(self):
        return f"Stack: {self.data.arr[:self.data.length]}"

    # Return True if the stack contains no elements
    def is_empty(self):
        return len(self) == 0

    # Push a value onto the top of the stack
    # (Adds element to the end of the underlying array)
    def push(self, value):
        self.data.append(value)

    # Remove and return the top element of the stack
    # Raises IndexError if the stack is empty
    def pop(self):
        return self.data.pop()

    # Return the top element without removing it
    # Raises IndexError if the stack is empty
    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek on empty stack. ")
        else:
            return self.data.access_element_by_index(self.data.length - 1)
