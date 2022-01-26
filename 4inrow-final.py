# █▀▀ █▀█ █▀▀ █▀▄ █ ▀█▀ █▀ 
# █▄▄ █▀▄ ██▄ █▄▀ █ ░█░ ▄█ 
# Amir Mohammadkhah - Heuristic
# Amirmohammad Omidi - Game Mechanics - GUI
# Hossein - Negamax
import numpy as np
import random
import pygame
import sys
import math
import os 
 
ROW_COUNT = 6
COLUMN_COUNT = 7

PLAYER = 0
AI = 1

EMPTY = 0
PLAYER_PIECE = 1
AI_PIECE = 2

# Colors used by pygame  
GREEN = (70,206,105)
PURPLE = (40,42,54)
MAGENTA = (206,121,172) # player one's color
YELLOW = (241,250,140) # player tow's color

def create_board(): 
    board = np.zeros((ROW_COUNT,COLUMN_COUNT),dtype = np.int8)
    return board

def print_board(board): #$ Fixes the board orientation and prints the board 
    print(np.flip(board, 0))

def check_location_validity(board, column): #$ is_valid_location 
    return board[ROW_COUNT-1][column] == 0 # Checks if the top row of the respective column is equal to 0 or not
                                 # if it is then we are allowed to drop a piece there

def piece_drop(board, row, column, piece): #$ drop_piece
    board[row][column] = piece

# Check if the position has not been filled yet

def get_next_open_row(board, column): #$
    for r in range(ROW_COUNT):    # for every row in a given column
        if board[r][column] == 0: # return the first row that is no yet filled
            return r

def win(board, piece): #$ winning_move
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

def not_piece(piece):
    if piece==AI_PIECE :
        return PLAYER_PIECE
    else :
        return AI_PIECE

def is_terminal_state(board):
	return win(board, PLAYER_PIECE) or win(board, AI_PIECE) or len(get_valid_locations(board)) == 0

def negamax(board,depth,alpha,beta,color,piece):
    
    is_terminal = is_terminal_state(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if win(board , piece) :
                return (None , math.inf)
            elif win(board , not_piece(piece)):
                return (None,-math.inf)
            else: # Game is over, no more valid moves
                return (None , 0)
        #else : # depth is 0 
        return(None ,color*heuristic(board))

    value = -math.inf
    valid_locations = get_valid_locations(board)
    column = random.choice(valid_locations)
    for col in valid_locations :
        row = get_next_open_row(board , col)
        b_copy = board.copy()
        piece_drop(b_copy, row,col,piece)
        new_value = -negamax(b_copy ,depth-1,-beta , -alpha , -color, not_piece(piece))[1] #without_max
        if(new_value > value):
            value = new_value
            column = col 
        alpha = max(alpha , value)
        if(alpha>= beta):
            break #cut_of
    return column , value 

def heuristic(matris):
    
    def win_modes(matris, piece):
        check = [0 , piece]
        new_way = 0
        # check horizantally 
        for c in range(COLUMN_COUNT-3):
            for r in range(ROW_COUNT):
                if (matris[r][c] in check) and (matris[r][c+1] in check) and (matris[r][c+2] in check) and (matris[r][c+3] in check): 
                    new_way = new_way + 1 
        
        # check vertically 
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT-3):
                if (matris[r][c] in check) and (matris[r+1][c] in check) and (matris[r+2][c] in check) and (matris[r+3][c] in check):    
                    new_way = new_way + 1 
        
        # check positively sloped diagonal
        for c in range(COLUMN_COUNT-3):
            for r in range(ROW_COUNT-3):
                if (matris[r][c] in check) and (matris[r+1][c+1] in check) and (matris[r+2][c+2] in check) and (matris[r+3][c+3] in check):    
                    new_way = new_way + 1   
        
        # check negetively sloped diagonal
        for c in range(COLUMN_COUNT-3):
                for r in range(3, ROW_COUNT):
                    if (matris[r][c] in check) and (matris[r-1][c+1] in check) and (matris[r-2][c+2] in check) and (matris[r-3][c+3] in check):    
                        new_way = new_way + 1    
        return new_way

    if win(matris , AI_PIECE):
        return math.inf
    elif win(matris , PLAYER_PIECE):
        return -math.inf

    Our_win_modes = win_modes(matris , AI_PIECE)
    oponent_win_modes = win_modes(matris , PLAYER_PIECE)
    score = Our_win_modes - oponent_win_modes 
    return score

def get_valid_locations(board): #true
	valid_locations = []
	for col in range(COLUMN_COUNT):
		if check_location_validity(board, col):
			valid_locations.append(col)
	return valid_locations

def draw_board(board): # draw the board 
    for c in range(COLUMN_COUNT): 
        for r in range(ROW_COUNT):
            # rect(surface, color, rect, width=0) - r*SQUARESIZE+SQUARESIZE --> shift down by one 
            pygame.draw.rect(screen, GREEN, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE)) # (Width,Height,Y,X)
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

pygame.init()
pygame.mixer.init() # For sound!

SQUARESIZE = 90
RADIUS = int(SQUARESIZE/2 - 5) # RADIUS of the circles (-5 so that the circles arent touching)
height = (ROW_COUNT+1) * SQUARESIZE
width = COLUMN_COUNT * SQUARESIZE
size = (width, height)
screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()
font = pygame.font.SysFont("Noto Sans Mono", 65)
pygame.draw.rect(screen, PURPLE, (0,0, width, SQUARESIZE)) # Prevents top row from getting black (There should be a better solution for this!)
# Sound files
drop_sound = pygame.mixer.Sound("sound/stone-drop.ogg")
win_sound = pygame.mixer.Sound("sound/tada.ogg")  
turn = PLAYER #random.randint(PLAYER,AI)

while not game_over:
    # os.system('cls' if os.name == 'nt' else 'clear') # Linux users exist too!
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, PURPLE, (0,0, width, SQUARESIZE))
            pos = event.pos[0] 
            if turn == PLAYER:
                pygame.draw.circle(screen, MAGENTA, (pos, int(SQUARESIZE/2)), RADIUS)
                
        pygame.display.update()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            drop_sound.play()
            pygame.draw.rect(screen, PURPLE, (0,0, width, SQUARESIZE))
			#print(event.pos)
			# Ask for Player 1 Input
            if turn == PLAYER:
                pos = event.pos[0] # To track our mouse movement
                col = int(math.floor(pos/SQUARESIZE)) # round down the number you get from pos/SQUARESIZE
                                                      # to determine which column we are in
                if check_location_validity(board, col):
                    row = get_next_open_row(board, col)
                    piece_drop(board, row, col, PLAYER_PIECE)
                    
                    if win(board, PLAYER_PIECE):
                        #os.system('cls' if os.name == 'nt' else 'clear')
                        label = font.render("Player one wins!", 1, MAGENTA)
                        screen.blit(label, (5,0)) # Blit --> Just updates a certain part of the screen (based on x, y position)
                        print("Player One Wins!")
                        game_over = True
                        
                    turn += 1
                    turn = turn % 2
                    
                    print_board(board)
                    draw_board(board)

	# # Ask for Player 2 Input
    if turn == AI and not game_over:				

		#col = random.randint(0, COLUMN_COUNT-1)
		#col = pick_best_move(board, AI_PIECE)
        col, minimax_score = negamax(board, 4, -math.inf, math.inf, 1, AI_PIECE) #negamax / minimax
        if check_location_validity(board, col):
            row = get_next_open_row(board, col)
            drop_sound.play()
            piece_drop(board, row, col, AI_PIECE)
            
            if win(board, AI_PIECE):
                # os.system('cls' if os.name == 'nt' else 'clear')
                label = font.render("Player two wins!", 1, YELLOW)
                screen.blit(label, (5,0)) 
                print("Player Two Wins!")
                game_over = True
                
            print_board(board)
            draw_board(board)
            
            turn += 1
            turn = turn % 2 # Alternate between zero and one
                            # (Player one and player two's turn respectively)    
    if game_over:
        win_sound.play()
        pygame.time.wait(5000) # If the game is over wait 5s then exit