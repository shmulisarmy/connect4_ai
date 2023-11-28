from main import win, tie, row_heights

def minimax(is_mp, board, depth):
    print(row_heights)
    print('\n'*5 + 'board')
    for row in board:
        print(*row, sep = ' ')
    if is_mp: 
        best_score = -depth
        for j in range(6):
            i = row_heights[j]
            if row_heights[j] < 0:
                continue
            if board[i][j] == ' ':
                board[i][j] = 'O'
                row_heights[j] -= 1
                if win(i, j, 'O'):
                    row_heights[j] += 1
                    board[i][j] = ' '
                    return depth
                if depth <= 0:
                    row_heights[j] += 1
                    board[i][j] = ' '
                    return 0
                score = 0 if tie() else minimax(False, board, depth - 1)
                row_heights[j] += 1
                board[i][j] = ' '
                best_score = max(best_score, score)
                
    else:
        best_score = depth

        for j in range(6):
            i = row_heights[j]
            if row_heights[j] < 0:
                continue
            if board[i][j] == ' ':
                board[i][j] = 'X'
                row_heights[j] -= 1
                if win(i, j, 'X'):
                    row_heights[j] += 1
                    board[i][j] = ' '
                    return -depth
                    
                if depth <= 0:
                    row_heights[j] += 1
                    board[i][j] = ' '
                    return 0
                score = 0 if tie() else minimax(True, board, depth-1)
                #restore position
                row_heights[j] += 1
                board[i][j] = ' '
                best_score = min(best_score, score)

    return best_score

def get_best_move(board, depth = 5):
    best_score = -depth
    
    for j in range(6):
        i = row_heights[j]
        if row_heights[j] < 0:
            continue
        if board[i][j] == ' ':
            board[i][j] = 'O'
            row_heights[j] -= 1
            if win(i, j, 'O'):
                row_heights[j] += 1
                board[i][j] = ' '
                return (i, j)
                
            score = 0 if tie() else minimax(False, board, depth-1)
            #restore position
            row_heights[j] += 1
            board[i][j] = ' '
            if score > best_score:
                best_score = score
                move = (i, j)
    return move

if __name__ == '__main__':
    row_heights = [5 for _ in range(7)]
    board = [[' ' for _ in range(7)] for _ in range(6)]


    max_depth = 3
    print(get_best_move(board))
    for row in board:
        print(*row, sep = ' ')
    print(row_heights)

