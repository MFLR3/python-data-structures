# Graph problems
from graph import Graph
letters = "ABCDEFGH"

# Setup & Initialization
print("# Setup & Initialization")
g = Graph()
print(f"Graph: {g}")
# Add Vertices
print("\n# Add Vertices")
for letter in letters:
    g.add_vertex(letter)
print(f"Graph: {g}")

# Add Edges (Normal Case)
print("\n# Add Edges (Normal Case)")
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "C")
g.add_edge("B", "E")
g.add_edge("B", "H")
g.add_edge("C", "H")
g.add_edge("C", "D")
print(g)

# Add Edge Error Case
print("\n# Add Edge Error Case")
try:
    g.add_edge("A", "Z")
except ValueError as e:
    print(f"Error: {e}")

# Remove Edge
print("\n# Remove Edge")
g.remove_edge("A", "B")
print("Edge removed between A and B: ")
print(g)

# Remove Edge Error Case
print("\n# Remove Edge Error Case")
try:
    g.remove_edge("A", "H")
except ValueError as e:
    print(f"Error: {e}")

# Remove Vertex
print("\n# Remove Vertex")
g.remove_vertex("C")
print("Vertex C removed: ")
print(g)

# Remove Vertex Error Case
print("\n# Remove Vertex Error Case")
try:
    g.remove_vertex("M")
except ValueError as e:
    print(f"Error: {e}")

# Vertex removal and length
print("\n# Vertex removal and length")
for vertex in list(g.adj_list):
    print(f"\nNumber of vertices before removal: {len(g.adj_list)}")
    g.remove_vertex(vertex)
    print(f"Number of vertices after removal: {len(g.adj_list)}")
    print(g)

print(f"Final graph state: {g}")
