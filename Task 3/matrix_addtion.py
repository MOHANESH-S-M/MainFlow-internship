# this is Task 3 question no 21
"""21. Matrix Addition
 Objective   : Add two matrices of the same dimensions.
 Input       : Two 2D lists (matrices) of integers.
 Output      : A 2D list containing the sum of corresponding elements.
 Hint        : Use nested loops to iterate through rows and columns, adding corresponding elements."""
def matrix_addition(a,b):
    if len(a) != len(b) or len(a[0])!= len(b[0]):
        raise ValueError("provide valid length for rows and columns")
    result = [[0,0,0],
              [0,0,0],
              [0,0,0]]
    for i in range(len(a)):
        for j in range(len(a[0])):
            result[i][j] = a[i][j] + b[i][j]
    return result
a = [[1,2,3],
     [4,5,6],
     [7,8,9]]
b = [[9,8,7],
     [6,5,4],
     [3,2,1]]
print(matrix_addition(a,b))
