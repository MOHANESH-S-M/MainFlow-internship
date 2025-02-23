# This is task 5
"""39. Sudoku Validator
 Objective        : Validate whether a given Sudoku board configuration is valid.
 Input            : A 9x9 2D list representing a Sudoku board.
 Output           : True if valid, otherwise False.
 Hint             : Check rows, columns, and 3×33 \times 33×3 grids for duplicates."""

def sudoku_validator(board):
    """ this is a sudoku validator where the input is taken as 9 X 9 grid where the 
        validator validates the whole grid and sub grids"""
    def is_validate(part):
        seen = set()
        for num in part:
            if num != '.':
                if num in seen :
                    return False
                seen.add(num)
        return True
    
    # checking rows
    for row in board:
        if not is_validate(row):
            return False
    
    # for columns
    for col_index in range(9):
        column = [board[row][col_index] for row in range(9)]
        if not is_validate(column):
            return False
    
    # for Subgrids
    for i in range(0,9,3):
        for j in range(0,9,3):
            subgrid =[board[row][column] for row in range(i,i+3) for column in range(j,j+3)]
            if not is_validate(subgrid):
                return False
    return True
# Example usage:
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

print(sudoku_validator(valid_board))
print(sudoku_validator(invalid_board)
)    