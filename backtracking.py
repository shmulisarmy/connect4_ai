import time, copy

def valid(row, col, num, board_copy):
    if num in board_copy[row]:
        return False
    for i in range(9):
        if board_copy[i][col] == num:
            return False
        
    newrow = (row//3)*3
    newcol = (col//3)*3

    for i in range(newrow, newrow+3):
        for j in range(newcol, newcol+3):
            if board_copy[i][j] == num:
                return False
            
    return True

def solve(board_copy, test = True):
    for row in range(9):
        for col in range(9):
            if board_copy[row][col]:
                temp = board_copy[row][col]
                board_copy[row][col] = 0
                if not valid(row, col, temp, board_copy):
                    board_copy[row][col] = temp
                    return False
                board_copy[row][col] = temp
                continue
            for num in range(1, 10):
                if valid(row, col, num, board_copy):
                    board_copy[row][col] = num
                    if not test:
                        print()
                        for row in board_copy:
                            print(*row, sep = ' ')
                    if solve(board_copy):
                        return True
                    board_copy[row][col] = 0
            return False
            
    return True

board = [[0 for i in range(9)]for i in range(9)]


while True:
    for row in board:
        print(*row, sep = ' ')
    row = input('row: ')
    if row == 'finish':
        solve(board, test = False)
        break
    row = int(row)-1
    col = int(input('col: '))-1
    num = int(input('num: '))

    board_copy = copy.deepcopy(board)

    if not valid(row, col, num, board_copy):
        print('thats an ileagle')

    board_copy[row][col] = num

    if solve(board_copy):
        board[row][col] = num
    else:
        print('not valid')