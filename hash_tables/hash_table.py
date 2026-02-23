# Hash Table

class HashTable:
    # Initialize an empty hash table.
    def __init__(self):
        self.table = {}

    # Return an unambiguous string representation of the HashTable object.
    def __repr__(self):
        return f"HashTable{self.table}"

    # Insert or update a key-value pair in the hash table.
    def __setitem__(self, key, value):
        self.table[key] = value

    # Retrieve the value associated with a key.
    def __getitem__(self, key):
        return self.table[key]

    # Remove a key-value pair from the hash table.
    def __delitem__(self, key):
        del self.table[key]

    # Return True if the key exists in the hash table.
    def __contains__(self, key):
        return key in self.table

    # Return the number of key-value pairs stored in the hash table.
    def __len__(self):
        return len(self.table)

    # Return a user-friendly string representation of the hash table.
    # Intended for readable display output.
    def __str__(self):
        return str(self.table)

    # Return the value for a key if it exists.
    def get(self, key, default=None):
        return self.table.get(key, default)

    # Return a dynamic view of all keys in the hash table.
    def keys(self):
        return self.table.keys()

    # Return a dynamic view of all values in the hash table.
    def values(self):
        return self.table.values()

    # Return a dynamic view of all key-value pairs as (key, value) tuples.
    def items(self):
        return self.table.items()

    # Remove all key-value pairs from the hash table.
    def reset(self):
        self.table.clear()
