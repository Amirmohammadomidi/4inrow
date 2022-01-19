import numpy as np
import os
import pygame
import sys
import math

COLUMN_COUNT = 7
ROW_COUNT = 6
# Colors used by pygame  
GREEN = (70,206,105)
PURPLE = (40,42,54)
MAGENTA = (206,121,172)
YELLOW = (241,250,140)

def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

def print_board(board): # Fixes the board orientation and prints the board 
    print(np.flip(board, 0))

def check_location_validity(board, column):
    return board[ROW_COUNT-1][column] == 0 # Checks if the top row of the respective column is equal to 0 or not
                                 # if it is then we are allowed to drop a piece there

def piece_drop(board, row, column, piece):
    board[row][column] = piece

# Check if the position has not been filled yet
def get_next_open_row(board, column):
    for r in range(ROW_COUNT):    # for every row in a given column
        if board[r][column] == 0: # return the first row that is no yet filled
            return r

def win(board, piece):
    # check horizantally 
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece: # draw the main rectangle
                return True
               
    
    # check vertically 
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:    
                return True  
    
    # check positively sloped diagenal
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:    
                return True  
    
    # check negetively sloped diagenal
    for c in range(COLUMN_COUNT-3):
            for r in range(3, ROW_COUNT):
                if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:    
                    return True     

def draw_board(board): # draw the board 
    pygame.draw.rect(screen, PURPLE, (0,0, width, SQUARESIZE)) # Created the first row here so it wouldn't be black when no input is given
    for c in range(COLUMN_COUNT): 
        for r in range(ROW_COUNT):
            # rect(surface, color, rect, width=0) - r*SQUARESIZE+SQUARESIZE --> shift down by one
            pygame.draw.rect(screen, GREEN, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE)) 
            # circle(surface, color, center, radius)
            pygame.draw.circle(screen, PURPLE, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS) # 
    
    for c in range(COLUMN_COUNT): 
        for r in range(ROW_COUNT):            
            if board[r][c] == 1:
                pygame.draw.circle(screen, MAGENTA, (int(c*SQUARESIZE+SQUARESIZE/2), height - int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS) 
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height - int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
    pygame.display.update()
            
board = create_board()
game_over = False
turn = 0

pygame.init()

SQUARESIZE = 90
RADIUS = int(SQUARESIZE/2 - 5) # RADIUS of the circles (-5 so the circles arent touching)
height = (ROW_COUNT+1) * SQUARESIZE
width = COLUMN_COUNT * SQUARESIZE
size = (width, height)
screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()
font = pygame.font.SysFont("Noto Sans Mono", 65)


while not game_over:
    print_board(board)
    os.system('cls' if os.name == 'nt' else 'clear') # Linux users exist too! ;-)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Quit when the user press the exit button
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, PURPLE, (0,0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, MAGENTA, (posx, int(SQUARESIZE/2)), RADIUS)
            else: 
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN: # Droping a piece when user press the mouse button
            pygame.draw.rect(screen, PURPLE, (0,0, width, SQUARESIZE)) # Clear the first row(rectangle) to make it pretty while showing which player won
            # Ask for player one's input
            # If turn == 0 then ask for player one's input 
            # Otherwise ask for player two's input
            if turn == 0:
                posx = event.pos[0]
                column = int(math.floor(posx/SQUARESIZE))

                if check_location_validity(board, column):
                    row = get_next_open_row(board, column)
                    piece_drop(board, row, column, 1)

                    if win(board, 1):
                        # os.system('cls' if os.name == 'nt' else 'clear')
                        label = font.render("Player One Wins!", 1, MAGENTA)
                        screen.blit(label, (5,0)) # blit --> update just the given part of the screen
                        print("Player One Wins!")
                        game_over = True

            # Ask for player two's input
            else:
                posx = event.pos[0]
                column = int(math.floor(posx/SQUARESIZE))

                if check_location_validity(board, column):
                    row = get_next_open_row(board, column)
                    piece_drop(board, row, column, 2)

                    if win(board, 2):
                        # os.system('cls' if os.name == 'nt' else 'clear')
                        label = font.render("Player Two Wins!", 1, YELLOW)
                        screen.blit(label, (5,0)) # blit --> update just the given part of the screen
                        print("Player Two Wins!")
                        game_over = True
            
            draw_board(board)

            if game_over:
                pygame.time.wait(5000) # If the game is over wait 5s then exit

            turn += 1
            turn = turn % 2 # Alternate between zero and one
                            # (Player one and player two's turn respectively)