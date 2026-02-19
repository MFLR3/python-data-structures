# Breadth-First Search (BFS) and Depth-First Search (DFS)
# Implemented using custom Queue and Stack classes.
# Both functions return a list representing traversal order.
# Assumes graph is represented as an adjacency list:
# graph.adj_list = { vertex: [neighbors] }
from queues.queue import Queue
from stacks.stack import Stack


def bfs(start, graph):
    # Set to track discovered vertices (prevents cycles)
    visited = set()
    # Queue controls FIFO traversal (level-by-level exploration)
    traversal_que = Queue()
    # Stores final traversal order
    result = []
    if start not in graph.adj_list:
        raise ValueError("Start node does not exist. ")
    # Begin traversal from the starting vertex
    traversal_que.enqueue(start)
    # Mark as visited immediately to avoid duplicate enqueues
    visited.add(start)
    # Continue processing while there are vertices to explore
    while not traversal_que.is_empty():
        # Remove next vertex in FIFO order
        current = traversal_que.dequeue()
        # Record visit order
        result.append(current)
        # Explore all adjacent vertices
        for neighbour in graph.adj_list[current]:
            # Only enqueue vertices not yet discovered
            # Prevents infinite loops in cyclic graphs
            if neighbour not in visited:
                traversal_que.enqueue(neighbour)
                visited.add(neighbour)
    return result


def dfs(start, graph):
    # Tracks visited vertices to prevent revisiting
    visited = set()
    # Stack controls LIFO traversal (deep exploration first)
    traversal_stack = Stack()
    # Stores traversal order
    result = []
    if start not in graph.adj_list:
        raise ValueError("Start node does not exist. ")
    # Initialize traversal by pushing start vertex onto stack
    traversal_stack.push(start)
    # Process vertices until stack is empty
    while not traversal_stack.is_empty():
        # Pop most recently added vertex (LIFO behavior)
        current = traversal_stack.pop()
        # Only process vertex if it hasn't been visited
        if current not in visited:
            # Mark as visited and record traversal
            visited.add(current)
            result.append(current)
            # Push neighbors onto stack for further exploration
            # Reversed to preserve natural left-to-right traversal order
            # (matches recursive DFS behavior)
            for neighbour in reversed(graph.adj_list[current]):
                # Only push unvisited vertices to avoid redundant processing
                if neighbour not in visited:
                    traversal_stack.push(neighbour)
    return result
