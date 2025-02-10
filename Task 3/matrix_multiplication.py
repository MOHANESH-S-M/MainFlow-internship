#This is Task 3 
"""22. Matrix Multiplication
 Objective  : Multiply two matrices AAA and BBB.
 Input      : Two 2D lists where the number of columns in AAA equals the number of rows in BBB.
 Output     : A 2D list representing the product matrix.
 Hint       : Multiply elements row-by-column and sum for each position in the result matrix."""
def mat_mul(a,b):
    row_a = len(a)
    col_a = len(a[0])
    row_b = len(b)
    col_b = len(b[0])
    if col_a != row_b:
        raise ValueError("Multiplication cant br performed due to in valid length")
    matrix_result = [[0 for _ in range(col_b)] for _ in range(row_a)]
    for i in range(row_a):
        for j in range(col_b):
            for k in range(col_a):
                matrix_result[i][j]+= a[i][k]*b[k][j]
    return matrix_result
a = [[1,2,3],
     [4,5,6],
     [7,8,9]]
b = [[9,8,7],
     [6,5,4],
     [3,2,1]]
print(mat_mul(a,b))