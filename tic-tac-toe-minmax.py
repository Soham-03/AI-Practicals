def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def get_free_positions(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

def minimax(board, depth, is_maximizing):
    if is_winner(board, 'O'):
        return 1
    if is_winner(board, 'X'):
        return -1
    if not get_free_positions(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for (r, c) in get_free_positions(board):
            board[r][c] = 'O'
            score = minimax(board, depth + 1, False)
            board[r][c] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for (r, c) in get_free_positions(board):
            board[r][c] = 'X'
            score = minimax(board, depth + 1, True)
            board[r][c] = ' '
            best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -float('inf')
    move = None
    for (r, c) in get_free_positions(board):
        board[r][c] = 'O'
        score = minimax(board, 0, False)
        board[r][c] = ' '
        if score > best_score:
            best_score = score
            move = (r, c)
    return move

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        if is_winner(board, 'O'):
            print("O wins!")
            break
        if is_winner(board, 'X'):
            print("X wins!")
            break
        if not get_free_positions(board):
            print("It's a draw!")
            break

        if current_player == 'X':
            row, col = map(int, input("Enter row and column numbers to place your X (0-2 each): ").split())
            if (row, col) in get_free_positions(board):
                board[row][col] = 'X'
                current_player = 'O'
        else:
            print("Computer's turn:")
            move = best_move(board)
            if move:
                board[move[0]][move[1]] = 'O'
                current_player = 'X'

if __name__ == "__main__":
    main()
4