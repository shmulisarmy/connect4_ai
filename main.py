import pygame as pg

def display_board():
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            pg.draw.circle(window, BLACK, ((j + 1/2) * piece_size, (i + 1/2 + 1) * piece_size), piece_size/2.5)
            if col == 'O':
                pg.draw.circle(window, RED, ((j + 1/2) * piece_size, (i + 1/2 + 1) * piece_size), piece_size/2.5)
            if col == 'X':
                pg.draw.circle(window, YELLOW, ((j + 1/2) * piece_size, (i + 1/2 + 1) * piece_size), piece_size/2.5)

def other_displays(row):
    pg.draw.rect(window, BLACK, pg.Rect(0, 0, width, piece_size))
    if player == 'O':
        pg.draw.circle(window, RED, ((row + 1/2) * piece_size, piece_size/2), piece_size/2)
    if player == 'X':
        pg.draw.circle(window, YELLOW, ((row + 1/2) * piece_size, piece_size/2), piece_size/2)


def win(height, row, cur_player):
    dhdr = [(0, 1), (1, 0), (1, 1), (-1, 1)]
    for dh, dr in dhdr:
        connections = 0
        for i in range(-3, 4):
            if -1 < height + dh*i < 6 and -1 < row + dr*i < 7 and board[height + dh*i][row + dr*i] == cur_player:
                connections += 1
                if connections == 4:
                    return True
            else:
                connections = 0
                if i >= 0:
                    break
def tie():
    for row in board:
        if any(i == ' ' for i in row):
            return False
        
    return True

BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (0, 255, 50)
piece_size = 20
width, height = piece_size*7, piece_size*7
window = pg.display.set_mode((width, height))
board_image = pg.image.load('board.png')                    
row_heights = [5 for _ in range(7)]
board = [[' ' for _ in range(7)] for _ in range(6)]
player = 'X'

while True:
    mx, my = pg.mouse.get_pos()

    row = mx//piece_size

    window.fill('blue')
    display_board()
    other_displays(row)
    pg.display.update()


    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.MOUSEBUTTONDOWN:
            if row_heights[row] >= 0:
                board[row_heights[row]][row] = player

                if win(row_heights[row], row, player):
                    display_board()
                    print("Player", player, "wins!")
    
                row_heights[row] -= 1
                player = 'X' if player == 'O' else 'O'