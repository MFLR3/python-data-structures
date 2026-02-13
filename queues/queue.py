# Queue
import arrays_lists.dynamic_arrays as da


class Queue:
    # Initialize an empty queue using DynamicArrays for storage
    def __init__(self):
        self.data = da.DynamicArrays()

    # Return the number of elements currently in the queue
    def __len__(self):
        return len(self.data)

    # Return a readable string representation of the queue
    def __str__(self):
        return f"Queue: {self.data.arr}"

    # Add a value to the back of the queue (FIFO insertion)
    def enqueue(self, value):
        self.data.append(value)

    # Remove and return the value at the front of the queue
    # Raises IndexError if the queue is empty
    def dequeue(self):
        if not self.is_empty():
            value = self.data.access_element_by_index(0)
            self.data.remove_at_index(0)
            return value
        else:
            raise IndexError("Cannot remove from empty queue.")

    # Return the value at the front without removing it
    # Raises IndexError if the queue is empty
    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek on empty queue. ")
        else:
            return self.data.access_element_by_index(0)

    # Return True if the queue contains no elements
    def is_empty(self):
        return len(self) == 0

    # Reset all values to default
    def reset(self):
        self.data.reset()
