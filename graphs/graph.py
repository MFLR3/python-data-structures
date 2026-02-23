# Graph


class Graph:
    # Initializes an empty graph using an adjacency list representation.
    # The adjacency list is a dictionary:
    #   key   > vertex
    #   value > list of connected vertices (neighbours)
    def __init__(self):
        self.adj_list = {}

    # Returns a readable string representation of the graph.
    # Each line shows a vertex and its list of connected neighbours.
    def __str__(self):
        list_string = ""
        for item in self.adj_list:
            list_string += f"{item}: {self.adj_list[item]}\n"
        return list_string.strip()

    # Adds a new vertex to the graph.
    # If the vertex already exists, duplicates are not allowed.
    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
        else:
            print("Cannot add duplicates")

    # Adds an undirected edge between two vertices.
    # Both vertices must already exist.
    # Ensures no duplicate edges are created.
    def add_edge(self, v1, v2):
        if v1 == v2:
            raise ValueError("Self-loops are not allowed. ")
        if v1 not in self.adj_list or v2 not in self.adj_list:
            raise ValueError("One or more vertices do not currently exist.")
        if v2 not in self.adj_list[v1]:
            self.adj_list[v1].append(v2)
        if v1 not in self.adj_list[v2]:
            self.adj_list[v2].append(v1)

    # Removes an undirected edge between two vertices.
    # Raises an error if either vertex does not exist or the edge is missing.
    def remove_edge(self, v1, v2):
        if v1 not in self.adj_list or v2 not in self.adj_list:
            raise ValueError("Missing vertex/vertices. ")
        if v1 in self.adj_list[v2] and v2 in self.adj_list[v1]:
            self.adj_list[v2].remove(v1)
            self.adj_list[v1].remove(v2)
        else:
            raise ValueError("Edge does not exist")

    # Removes a vertex from the graph.
    # First removes all edges connected to the vertex,
    # then deletes the vertex from the adjacency list.
    def remove_vertex(self, vertex):
        if vertex not in self.adj_list:
            raise ValueError("Missing vertex. ")
        for neighbour in self.adj_list[vertex]:
            if vertex in self.adj_list[neighbour]:
                self.adj_list[neighbour].remove(vertex)
        del self.adj_list[vertex]
