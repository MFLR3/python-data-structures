# Dynamic Arrays
class DynamicArrays:
    # Initializes the dynamic array with a fixed starting capacity, zero length, and an underlying list.
    def __init__(self):
        self.capacity = 4
        self.length = 0
        self.arr = [None] * self.capacity

    # Returns the number of elements currently stored in the array.
    def __len__(self):
        return self.length

    # Returns the element at a given index if it’s within bounds.
    def access_element_by_index(self, index):
        if 0 <= index < self.length:
            return self.arr[index]
        else:
            raise IndexError("Out of bounds.")

    # Creates and returns a new underlying array with a specified capacity, copying existing elements.
    def resize(self, capacity):
        new_arr = [None] * capacity
        for i in range(self.length):
            new_arr[i] = self.arr[i]
        return new_arr

    # Adds an element to the end of the array, resizing if capacity is reached.
    def append(self, element):
        if self.length == self.capacity:
            self.capacity *= 2
            new_arr = self.resize(self.capacity)
            new_arr[self.length] = element
            self.arr = new_arr
        else:
            self.arr[self.length] = element
        self.length += 1

    # Removes and returns the last element, shrinking the array if usage drops too low.
    def pop(self):
        if self.length > 0:
            last_element = self.arr[self.length - 1]
            self.length -= 1
        else:
            raise IndexError("Array is empty, pop is not possible.")
        if (self.length <= (self.capacity // 4)) and (self.capacity > 4):
            self.capacity //= 2
            new_arr = self.resize(self.capacity)
            self.arr = new_arr
        else:
            self.arr[self.length] = None
        return last_element

    # Inserts an element at a specific index, shifting elements right and resizing if needed.
    def insert_at_index(self, index, element):
        if 0 <= index <= self.length:
            if self.length == self.capacity:
                self.capacity *= 2
                new_arr = self.resize(self.capacity)
                for i in range(self.length, index, -1):
                    new_arr[i] = new_arr[i - 1]
                new_arr[index] = element
                self.arr = new_arr
            else:
                for i in range(self.length, index, -1):
                    self.arr[i] = self.arr[i - 1]
                self.arr[index] = element
            self.length += 1
        else:
            raise IndexError("Index entered is out of bounds.")

    # Removes an element at a specific index, shifting elements left and shrinking if needed.
    def remove_at_index(self, index):
        if 0 <= index < self.length:
            if self.length > 0:
                new_arr = self.resize(self.capacity)
                for i in range(index, self.length - 1):
                    new_arr[i] = new_arr[i + 1]
                self.length -= 1
                if (self.length <= (self.capacity // 4)) and (self.capacity > 4):
                    self.capacity //= 2
                    new_arr = self.resize(self.capacity)
                    self.arr = new_arr
                else:
                    new_arr[self.length] = None
                    self.arr = new_arr
            else:
                raise IndexError("Array is empty, removing item is not possible.")
        else:
            raise IndexError("Index entered is out of bounds.")
