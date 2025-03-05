# This is Task 8
"""60. Find All Paths in a Graph
 Objective     : Find all possible paths between two nodes in a directed graph.
 Input         : A directed graph and two nodes (start and end).
 Output        : A list of lists, where each list is a path from start to end.
 Hint          : Use depth-first search (DFS) and backtracking to find all paths."""
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def find_all_paths(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]

        paths = []
        for node in self.graph[start]:
            if node not in path:
                new_paths = self.find_all_paths(node, end, path)
                paths.extend(new_paths)

        return paths

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)

print(g.find_all_paths(0, 3))  # Output: [[0, 1, 3], [0, 2, 3]]
