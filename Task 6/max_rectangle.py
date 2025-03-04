# This is Task 6
"""44. Maximal Rectangle in Binary Matrix
 Objective     : Find the area of the largest rectangle in a binary matrix (matrix containing only 0's and 1's).
 Input         : A 2D binary matrix.
 Output        : The area of the largest rectangle formed by 1's.
 Hint          : Use dynamic programming by treating each row as the base of a histogram and applying the largest
       kdmmmm          rectangle in histogram technique."""
def max_rectangle(matrix):
    if not matrix or not matrix[0]:
        return 0
    
    row, col = len(matrix), len(matrix[0])  # Fix column calculation
    height = [0] * col
    max_area = 0

    for rows in matrix:
        for j in range(col):
            height[j] = height[j] + 1 if int(rows[j]) == 1 else 0  # Convert string to int
        
        max_area = max(max_area, largest_rect(height))
    
    return max_area

def largest_rect(height):
    stack = []
    max_area = 0
    height.append(0)  # Sentinel to process all elements

    for i, h in enumerate(height):
        while stack and height[stack[-1]] > h:
            height_value = height[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height_value * width)

        stack.append(i)

    height.pop() 
    return max_area

matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]

print(max_rectangle(matrix))  

