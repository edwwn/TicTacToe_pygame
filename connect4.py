import numpy as np
import pygame
import sys
import math

BLUE=(0,0,255)
BLACK=(0,0,0)
RED=(255,0,0)
YELLOW=(255,255,0)

ROW_COUNT =6
COLUMN_COUNT=7

def create_board():
    board =np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col): 
    return board[ROW_COUNT-1][col]==0

def get_next_open_row(board,col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_baord(board):
    print(np.flip(board, 0))


def winning_move(board,piece):
    #check horizonatal laocaitons
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] ==piece and board[r][c+2]==piece and board[r][c+3]==piece:
                return True


    #check vertical laocaitons
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] ==piece and board[r+2][c]==piece and board[r+3][c]==piece:
                return True

    # Check for positively slopped
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] ==piece and board[r+2][c+2]==piece and board[r+3][c+3]==piece:
                return True


    # Check for negatively slopped 
    for c in range(COLUMN_COUNT-3):
        for r in range(3,ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] ==piece and board[r-2][c+2]==piece and board[r-3][c+3]==piece:
                return True

def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen,BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            if board[r][c]==0:
                pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[r][c]==1:
                 pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS) 
            else:
                 pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)     

    pygame.display.update()    

board=create_board()
game_over=False
turn = 0 
print_baord(board)
pygame.init()

SQUARESIZE=100

width = COLUMN_COUNT *SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE
size = (width,height)
RADIUS =int(SQUARESIZE/2 -5)


screen =pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()






while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN: 
            print(event.pos)
            #Ask for player 1 Intput
            if turn==0:
                posx=event.pos[0]
                col =int(math.floor(posx/SQUARESIZE))
                if is_valid_location(board,col):
                    row= get_next_open_row(board, col)
                    drop_piece(board,row,col,1)

                    if winning_move(board,1):
                        print("Player 1 Wins!!! Congrats!!!")
                        game_over=True

            #Ask for player 2 Input    
            else:
                posx=event.pos[0]
                col =int(math.floor(posx/SQUARESIZE))
                if is_valid_location(board,col):
                    row= get_next_open_row(board, col)
                    drop_piece(board,row,col,2)

                    if winning_move(board,1):
                        print("Player 2 Wins!!! Congrats!!!")
                        game_over=True
                        
            print_baord(board)   
            draw_board(board)
            
            turn +=1
            turn = turn % 2

