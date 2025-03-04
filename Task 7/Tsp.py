# This is Task 7
""" 49. Traveling Salesman Problem (TSP)
 Objective   : Find the shortest possible route that visits each city once and returns to the origin city.
 Input       : A list of cities and the distances between each pair of cities.
 Output      : The shortest possible route and its total distance.
 Hint        : Use dynamic programming or branch-and-bound for an approximate solution."""
from itertools import permutations

def tsp(graph):
    n = len(graph)
    all_vertices = set(range(n))
    min_cost = float('inf')
    best_path = []

    for perm in permutations(range(1, n)):
        cost = graph[0][perm[0]]  # Start from city 0
        for i in range(len(perm) - 1):
            cost += graph[perm[i]][perm[i + 1]]
        cost += graph[perm[-1]][0]  # Return to city 0

        if cost < min_cost:
            min_cost = cost
            best_path = [0] + list(perm) + [0]

    return best_path, min_cost

# Example
graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
print(tsp(graph))
