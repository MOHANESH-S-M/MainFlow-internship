# This is Task 7
""" 50. Graph Cycle Detection
 Objective   : Detect whether a graph contains a cycle.
 Input       : An undirected graph represented as an adjacency list.
 Output      : True if the graph contains a cycle, otherwise False.
 Hint        : Use depth-first search (DFS) with a recursion stack to detect cycles."""
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def is_cyclic_util(self, v, visited, parent):
        visited[v] = True
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                if self.is_cyclic_util(neighbor, visited, v):
                    return True
            elif parent != neighbor:
                return True
        return False

    def is_cyclic(self):
        visited = {i: False for i in self.graph}
        for node in self.graph:
            if not visited[node]:
                if self.is_cyclic_util(node, visited, -1):
                    return True
        return False

# Example
g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
print("Graph contains cycle:", g.is_cyclic())
