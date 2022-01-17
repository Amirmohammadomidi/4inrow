import numpy as np
import os

COLUMN_COUNT = 7
ROW_COUNT = 6

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
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece: 
                return True  
    
    # check vertically 
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:    
                return True  
    
    # check positively sloped diagenal
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:    
                return True  
    
    # check negetively sloped diagenal
    for c in range(COLUMN_COUNT-3):
            for r in range(3, ROW_COUNT):
                if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:    
                    return True     
                                                                                             
board = create_board()
game_over = False
turn = 0

while not game_over:
    os.system('cls' if os.name == 'nt' else 'clear') # Linux users exit too! ;-)
    print_board(board)
    # Ask for player one's input
    # If turn == 0 then ask for player one's input 
    # Otherwise ask for player two's input
    if turn == 0: 
        column = int(input("Player one's turn:")) 

        if check_location_validity(board, column):
            row = get_next_open_row(board, column)
            piece_drop(board, row, column, 1)

            if win(board, 1):
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Player One Wins!")
                game_over = True
                break

    # Ask for player two's input
    else:
        column = int(input("Player two's turn:"))

        if check_location_validity(board, column):
            row = get_next_open_row(board, column)
            piece_drop(board, row, column, 2)

            if win(board, 2):
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Player Two Wins!")
                game_over = True
                break

    turn += 1
    turn = turn % 2 # Alternate between zero and one
                    # (Player one and player two's turn respectively)