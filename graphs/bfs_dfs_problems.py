# BFS and DFS problems
from graph import Graph
import bfs_dfs
letters = "ABCDEFGH"


# Setup Graph
print("# Setup Graph")
g = Graph()
for letter in letters:
    g.add_vertex(letter)

g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "C")
g.add_edge("C", "D")
g.add_edge("D", "E")
g.add_edge("E", "F")
g.add_edge("F", "G")
g.add_edge("G", "H")
g.add_edge("F", "A")

# Print Graph
print("\n# Print Graph")
print(f"Graph: \n{g}")

# BFS Test
print("\n# BFS Test")
bfs_result = bfs_dfs.bfs("B", g)
print(f"Results for bfs traversal: {bfs_result}")

# DFS Test
print("\n# DFS Test")
dfs_result = bfs_dfs.dfs("B", g)
print(f"Results for dfs traversal: {dfs_result}")

# Different Start Node
print("\n# Different Start Node")
bfs_result = bfs_dfs.bfs("E", g)
print(f"Results for bfs traversal: {bfs_result}")
dfs_result = bfs_dfs.dfs("E", g)
print(f"Results for dfs traversal: {dfs_result}")

# Invalid Start Node
print("\n# Invalid Start Node")
try:
    bfs_result = bfs_dfs.bfs("Z", g)
except ValueError as e:
    print(f"Error: {e}")
try:
    dfs_result = bfs_dfs.dfs("Z", g)
except ValueError as e:
    print(f"Error: {e}")

# Disconnected Graph
print("\n# Disconnected Graph")
g.add_vertex("Z")
bfs_result = bfs_dfs.bfs("E", g)
print(f"Results for bfs traversal: {bfs_result}")
dfs_result = bfs_dfs.dfs("E", g)
print(f"Results for dfs traversal: {dfs_result}")

# Cycle Safety Test
print("\n# Cycle Safety Test")
h = Graph()
for letter in letters:
    h.add_vertex(letter)

h.add_edge("A", "B")
h.add_edge("B", "C")
h.add_edge("C", "D")
h.add_edge("D", "A")

bfs_result = bfs_dfs.bfs("B", h)
print(f"Results for bfs traversal: {bfs_result}")
dfs_result = bfs_dfs.dfs("B", h)
print(f"Results for dfs traversal: {dfs_result}")
