# Graph and bfs_dfs problems
from graph import Graph
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

g = Graph()
for item in alphabet:
    g.add_vertex(item)
    g.add_edge("A", item)


g.add_edge("B", "C")
g.add_edge("B", "E")
g.add_edge("B", "Z")

print(g)
g.remove_vertex('A')
print(g)