# This is Task 8 
""" 56. Maximum Flow in a Graph (Ford-Fulkerson)
 Objective   : Find the maximum flow in a flow network.
 Input       : A graph represented as an adjacency matrix and a source and sink node.
 Output      : The maximum flow from source to sink.
 Hint        : Use the Ford-Fulkerson algorithm with DFS or BFS to find augmenting paths."""
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]
    
    def add_edge(self, u, v, capacity):
        self.graph[u][v] = capacity

    def bfs(self, source, sink, parent):
        visited = [False] * self.V
        queue = [source]
        visited[source] = True

        while queue:
            u = queue.pop(0)

            for v, capacity in enumerate(self.graph[u]):
                if not visited[v] and capacity > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == sink:
                        return True
        return False

    def ford_fulkerson(self, source, sink):
        parent = [-1] * self.V
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float("Inf")
            v = sink
            while v != source:
                u = parent[v]
                path_flow = min(path_flow, self.graph[u][v])
                v = u

            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = u

            max_flow += path_flow

        return max_flow

# Example usage:
g = Graph(4)
g.add_edge(0, 1, 3)
g.add_edge(0, 2, 2)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 2)
g.add_edge(2, 3, 3)

print("Maximum Flow:", g.ford_fulkerson(0, 3))
