# This is Task 5
"""38. Rotate Matrix
 Objective            : Rotate a matrix 90 degrees clockwise.
 Input                : A 2D list (matrix).
 Output               : The rotated matrix.
 Hint                 : Transpose the matrix and then reverse rows."""
def rotate_matrix_90(mat):
    n =len(mat)
    for i in range(n):
        for j in range(i+1,n):
            mat[i][j],mat[j][i] = mat[j][i],mat[i][j]
    for i in range(n):
        for j in range(n//2):
            mat[i][j],mat[i][n-j-1] = mat[i][n-j-1],mat[i][j]
    return mat
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotated = rotate_matrix_90(matrix)
for row in rotated:
    print(row)
