#tthis is task 3 project
""" 3. AI-Based Tic-Tac-Toe
 ● Description     : Create a Tic-Tac-Toe game where the computer plays against the user and uses a minimax algorithm to make decisions.
 ● Challenges      : ○ Implement AI logic with decision trees.
                     ○ Handle edge cases like a full board or winning moves.
                     ○ Provide a user-friendly interface.
 ● Skills          : Game theory, recursion, and strategic thinking."""
import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
    print("-" * 9)

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 10 - depth
    if check_winner(board, 'X'):
        return depth - 10
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(best_score, score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    while True:
        row, col = map(int, input("Enter row and column (0-2): ").split())
        if board[row][col] != ' ':
            print("Invalid move, try again.")
            continue
        board[row][col] = 'X'
        print_board(board)  # Print board after player's move
        
        if check_winner(board, 'X'):
            print("You win!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        ai_move = best_move(board)
        board[ai_move[0]][ai_move[1]] = 'O'
        print_board(board)  # Print board after AI's move
        
        if check_winner(board, 'O'):
            print("AI wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
