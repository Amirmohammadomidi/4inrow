import numpy as np
import os

COLUMN_COUNT = 8
ROW_COUNT = 8

def create_board():
    board = np.zeros((8,8))
    return board

def print_board(board): # Fixes the board orientation and prints the board 
    print(np.flip(board, 0))

def check_location_validity(board, column):
    return board[7][column] == 0 # Checks if the top row of the respective column is equal to 0 or not
                                 # if it is then we are allowed to drop a piece there

def piece_drop(board, row, column, piece):
    board[row][column] = piece

# Check if the position has not been filled yet
def get_next_open_row(board, column):
    for r in range(ROW_COUNT):    # for every row in a given column
        if board[r][column] == 0: # return the first row that is no yet filled
            return r            

            
def game_over_condition(board):
    '''get matris and return "Has anyone won?" and who?'''
    win = False
    def chek_row(x , y , bord):
        for move in range(1 , 4):
            if bord[x][y] !=  bord[x][y + move]: #move in row
                return False
        return True #win

    def chek_colunm(x , y , bord): #move in colunm
        for move in range(1 , 4):
            if bord[x][y] !=  bord[x+ move][y]:
                return False
        return True #win

    def chek_movarab_rast(x , y , bord): 
        for move in range(1 , 4):
            if bord[x][y] !=  bord[x+ move][y + move]: # Move in diameter
                return False
        return True #win
    
    def chek_movarab_chap(x , y , bord): 
        for move in range(1 , 4):
            if bord[x][y] !=  bord[x + move][y - move]:  # Move in diameter
                return False
        return True #win

    for i in range (8): #move in row
        for j in range(8): # move in column
            if board[i][j] != 0 : #آیا مهره ای قرار دارد در این خانه
                if j in [0 , 1 , 2 , 3 , 4]: #در محدوده مجاز  است؟
                    win = chek_row(i , j  , board)
                    if win:
                        return [True  , board[i][j] ] # [کسی برنده است؟   , آیا برده ای وجود دارد؟]
                
                if i in [0 , 1 , 2 , 3 , 4 , 5 , 6]: #در محدوده مجاز  است؟
                    win = chek_colunm(i , j  , board)
                    if win:
                        return [True  , board[i][j] ] # [کسی برنده است؟   , آیا برده ای وجود دارد؟] 

                if  (i in [0 , 1 , 2 , 3, 4 ]) and (j in [0 , 1 , 2 , 3, 4]): #در محدوده مجاز  است؟
                    win = chek_movarab_rast(i, j , board)
                    if win :
                        return [True  , board[i][j] ] # [کسی برنده است؟   , آیا برده ای وجود دارد؟] 
                
                if  (j in [3, 4 , 5 , 6 , 7  ]) and (i in [0 , 1 , 2 , 3, 4 , 5]): #در محدوده مجاز  است؟
                    win = chek_movarab_chap(i, j , board)
                    if win :
                        return [True  , board[i][j] ] # [کسی برنده است؟   , آیا برده ای وجود دارد؟]
    
    return [False , None] # [کسی برنده است؟   , آیا برده ای وجود دارد؟] 
            
board = create_board()
win = False
turn = 0

while win == False:
    os.system( 'cls' ) # clear consol
    print_board(board)
    # Ask for player one's input
    # If turn == 0 then ask for player one's input 
    # Otherwise ask for player two's input
    if turn == 0: 
        column = int(input("Player one's turn:")) 

        if check_location_validity(board, column):
            row = get_next_open_row(board, column)
            piece_drop(board, row, column, 1)
            win = game_over_condition(board)[0]
            if win :
                os.system( 'cls' ) # clear consol
                print_board(board)
                print("win Player one" ) 
        
    # Ask for player two's input
    else:
        column = int(input("Player two's turn:"))

        if check_location_validity(board, column):
            row = get_next_open_row(board, column)
            piece_drop(board, row, column, 2)
            win = game_over_condition(board)[0]
            if win :
                os.system( 'cls' ) # clear consol
                print_board(board)
                print("win Player two" )
    

    turn += 1
    turn = turn % 2 # Alternate between zero and one
                    # (Player one and player two's turn respectively)             
