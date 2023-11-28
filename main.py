import pygame as pg, time, sys, colorama

def pb():
    for row in board:
        print('\n' + '-'*29, end = '\n| ')
        for col in row:
            if col == 'X':
                print(colorama.Fore.GREEN + col + colorama.Fore.RESET, end = ' | ')
            elif col == 'O':
                print(colorama.Fore.RED + col + colorama.Fore.RESET, end = ' | ')
            else:
                print(end = '  | ')
    print('\n' + '-'*29)


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
        for i in range(-4, 5):
            if -1 < height + dh*i < 8 and -1 < row + dr*i < 8 and board[height + dh*i][row + dr*i] == cur_player:
                connections += 1
                if connections == 5:
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

def drawing_logic():
    pb()

    window.fill('blue')
    display_board()
    other_displays(row)
    pg.display.update()

def new_game():
    return ([7 for _ in range(8)], [[' ' for _ in range(8)] for _ in range(8)], True)

BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (0, 255, 50)
piece_size = 80
if len(sys.argv) > 1:
    try:
        if 20 <= int(sys.argv[1]) <= 110:
            piece_size = int(sys.argv[1])
    except:
        pass
width, height = piece_size*8, piece_size*9
window = pg.display.set_mode((width, height))
pg.display.set_caption('connect5')
row_heights = [7 for _ in range(8)]
board = [[' ' for _ in range(8)] for _ in range(8)]
player = 'X'
one_piece_to_go = True

if __name__ == "__main__":
    while True:
        mx, my = pg.mouse.get_pos()
        row = mx//piece_size

        keys = pg.key.get_pressed()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.MOUSEBUTTONDOWN or keys[pg.K_SPACE]:
                time.sleep(0.1)
                if row_heights[row] >= 0:
                    for i in range(0, row_heights[row] + 1):
                        board[i][row] = player
                        drawing_logic()


                        time.sleep(.06)

                          if i == row_heights[row]:
                            break
                        board[i][row] = ' '

                    if win(row_heights[row], row, player):
                        drawing_logic()
                        print("Player", player, "wins!")
                        time.sleep(1)
                        row_heights, board, one_piece_to_go =  new_game()
        
                    else:
                        row_heights[row] -= 1
                        if one_piece_to_go:
                            player = 'X' if player == 'O' else 'O'
                            one_piece_to_go = False
                        else:
                            one_piece_to_go = True

        drawing_logic()