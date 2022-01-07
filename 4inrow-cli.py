import numpy as np

COLUMN_COUNT = 7
ROW_COUNT = 6

def create_board():
    board = np.zeros((6,7))
    return board

def print_board(board): # Fixes the board orientation and prints the board 
    print(np.flip(board, 0))

def check_location_validity(board, column):
    return board[5][column] == 0 # Checks if the top row of the respective column is equal to 0 or not
                                 # if it is then we are allowed to drop a piece there

def piece_drop(board, row, column, piece):
    board[row][column] = piece

# Check if the position has not been filled yet
def get_next_open_row(board, column):
    for r in range(ROW_COUNT):    # for every row in a given column
        if board[r][column] == 0: # return the first row that is no yet filled
            return r              
            
board = create_board()
print_board(board)
game_over = False
turn = 0

while not game_over:
    
    # Ask for player one's input
    # If turn == 0 then ask for player one's input 
    # Otherwise ask for player two's input
    if turn == 0: 
        column = int(input("Player one's turn:")) 

        if check_location_validity(board, column):
            row = get_next_open_row(board, column)
            piece_drop(board, row, column, 1)
        
    # Ask for player two's input
    else:
        column = int(input("Player two's turn:"))

        if check_location_validity(board, column):
            row = get_next_open_row(board, column)
            piece_drop(board, row, column, 2)
    
    print_board(board)
    turn += 1
    turn = turn % 2 # Alternate between zero and one
                    # (Player one and player two's turn respectively)
