#this is task 2 MAZE generator and SOLVER
""" 2. Maze Generator and Solver
 ● Description       : Build a program that generates random mazes and solves them using 
                       techniques like Depth-First Search (DFS) or Breadth-First Search (BFS).
 ● Challenges        :
                        ○ Represent the maze as a grid using nested lists.
                        ○ Implement logic to ensure generated mazes are solvable.
                        ○ Visualize the maze in the terminal with clear paths and walls.
 ● Skills            : Recursive algorithms, graph theory, and problem-solving.
 ● Restriction       : No use of external libraries for visualization or graphical rendering (like matplotlib, pygame).
 ● Reason            : This restriction ensures that students focus on core algorithmic logic rather
                        than visualizing the maze. The main objective is to implement algorithms like
                        Depth-First Search (DFS) or Breadth-First Search (BFS) to generate and solve mazes
                        programmatically. The visualization of the maze is secondary and can be achieved in a
                        simple text-based format (like using 1 for walls and 0 for paths).
 ● Learning Outcome  : Students will learn about graph traversal algorithms,
                        backtracking, and recursive thinking, which are fundamental concepts in computer science."""
import random

def initialize_maze(rows, cols):
    # Create a grid full of walls (1)
    return [[1 for _ in range(cols)] for _ in range(rows)]

def generate_maze(maze, start_row, start_col):
    directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]  # Down, Right, Up, Left
    maze[start_row][start_col] = 0  # Mark the starting cell as a path

    random.shuffle(directions)  # Shuffle directions for randomness
    for dr, dc in directions:
        new_row, new_col = start_row + dr, start_col + dc
        if 0 < new_row < len(maze) and 0 < new_col < len(maze[0]) and maze[new_row][new_col] == 1:
            # Carve a path between the current cell and the new cell
            maze[start_row + dr // 2][start_col + dc // 2] = 0
            maze[new_row][new_col] = 0
            generate_maze(maze, new_row, new_col)

def solve_maze(maze, start, end):
    queue = [start]
    visited = set()
    visited.add(start)
    parent = {start: None}

    while queue:
        current = queue.pop(0)
        if current == end:
            break

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_row, new_col = current[0] + dr, current[1] + dc
            if (0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and
                maze[new_row][new_col] == 0 and (new_row, new_col) not in visited):
                visited.add((new_row, new_col))
                parent[(new_row, new_col)] = current
                queue.append((new_row, new_col))

    # Backtrack to find the path
    path = []
    current = end
    while current:
        if current not in parent:  # Handle unreachable case
            print("No path found!")
            return []
        path.append(current)
        current = parent[current]
    path.reverse()
    return path

def display_maze(maze, start, end, path=None):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if (i, j) == start:
                print("S", end=" ")  # Start cell
            elif (i, j) == end:
                print("E", end=" ")  # End cell
            elif path and (i, j) in path:
                print("P", end=" ")  # Path cells
            elif maze[i][j] == 1:
                print("1", end=" ")  # Wall cells
            else:
                print("0", end=" ")  # Open cells
        print()

# Example usage
rows, cols = 20, 20  # Maze size
maze = initialize_maze(rows, cols)
generate_maze(maze, 1, 1)  # Start maze generation from (1, 1)

start, end = (1, 1), (rows-2, cols-2)
maze[end[0]][end[1]] = 0  # Ensure the end point is open

print("Generated Maze:")
display_maze(maze, start, end)  # Print the generated maze

path = solve_maze(maze, start, end)
if path:
    print("\nMaze with Solution Path:")
    display_maze(maze, start, end, path=path)  # Print the maze with the solution path
else:
    print("No path found!")

