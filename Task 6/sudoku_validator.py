# This is Task 6
""" 39. Sudoku Validator
 Objective: Validate whether a given Sudoku board configuration is valid.
 Input: A 9x9 2D list representing a Sudoku board.
 Output: True if valid, otherwise False.
 Hint: Check rows, columns, and 3×33 \times 33×3 grids for duplicates."""
def validate_sudoku(board):
    N = len(board)
    def validate(a_list):
        seen = set()
        for i in a_list:
            if i != '.':
                if i in seen:
                    return False
                seen.add(i)
        return True
    
    # for all rows
    for row in board:
        if not validate(row):
            return False
    # for column
    for col_index in range(9):
        column = [board[row][col_index] for row in range(9)]
        if not validate(column):
            return False
    # for sub grids 3x3
    for i in range(0,9,3):
        for j in range(0,9,3):
            subgrid =[board[row][column] for row in range(i,i+3) for column in range(j,j+3)]
            if not validate(subgrid):
                return False
    return True
valid_board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

invalid_board = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],  # Changed a '5' to '8'
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

print(validate_sudoku(valid_board))
print(validate_sudoku(invalid_board)
)    