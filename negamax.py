
def negamax(board,depth,alpha,beta,color): #uses scoreposition function 
    valid_locations = get_valid_locations(board)
    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(board , AI_PIECE) :
                return (None , color*100000000000000)
            elif winning_move(board , PLAYER_PIECE):
                return (None,color* -10000000000000)
            else: # Game is over, no more valid moves
                return (None , 0)
        else : # depth is 0 
            return(None ,color* score_position(board,AI_PIECE))
            
    value = -math.inf
    column = random.choice(valid_locations)
    for col in valid_locations :
        row = get_next_open_row(board , col)
        b_copy = board.copy()
        drop_piece(b_copy, row,col, AI_PIECE)
        new_value = -negamax(b_copy ,depth-1,-beta , -alpha , -color)[1] #without_max
        if(new_value > value):
            value = new_value
            column = col 
        alpha = max(alpha , value)
        if(alpha>= beta):
            break #cut_of
    return column , value

def negamax2(board,depth,alpha,beta,color): # use hiorestic function 
    valid_locations = get_valid_locations(board)
    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(board , AI_PIECE) :
                return (None , 100000000000000)
            elif winning_move(board , PLAYER_PIECE):
                return (None,-10000000000000)
            else: # Game is over, no more valid moves
                return (None , 0)
        else : # depth is 0 
            return(None ,color*hiorestic(board))
            
    value = -math.inf
    column = random.choice(valid_locations)
    for col in valid_locations :
        row = get_next_open_row(board , col)
        b_copy = board.copy()
        drop_piece(b_copy, row,col, AI_PIECE)
        new_value = -negamax(b_copy ,depth-1,-beta , -alpha , -color)[1] #without_max
        if(new_value > value):
            value = new_value
            column = col 
        alpha = max(alpha , value)
        if(alpha>= beta):
            break #cut_of
    return column , value 


def hiorestic(matris):
    
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

    if winning_move(matris , piece=2):
        return math.inf
    elif winning_move(matris , piece=1):
        return -math.inf

    Our_win_modes = win_modes(matris , piece=2)
    oponent_win_modes = win_modes(matris , piece=1)
    score = Our_win_modes - oponent_win_modes 
    return score

def minimax(board, depth, alpha, beta, maximizingPlayer): #with scorepos func
	valid_locations = get_valid_locations(board)
	is_terminal = is_terminal_node(board)
	if depth == 0 or is_terminal:
		if is_terminal:
			if winning_move(board, AI_PIECE):
				return (None, 100000000000000)
			elif winning_move(board, PLAYER_PIECE):
				return (None, -10000000000000)
			else: # Game is over, no more valid moves
				return (None, 0)
		else: # Depth is zero
			return (None, score_position(board, AI_PIECE))
	if maximizingPlayer:
		value = -math.inf
		column = random.choice(valid_locations)
		for col in valid_locations:
			row = get_next_open_row(board, col)
			b_copy = board.copy()
			drop_piece(b_copy, row, col, AI_PIECE)
			new_score = minimax(b_copy, depth-1, alpha, beta, False)[1]
			if new_score > value:
				value = new_score
				column = col
			alpha = max(alpha, value)
			if alpha >= beta:
				break
		return column, value

	else: # Minimizing player
		value = math.inf
		column = random.choice(valid_locations)
		for col in valid_locations:
			row = get_next_open_row(board, col)
			b_copy = board.copy()
			drop_piece(b_copy, row, col, PLAYER_PIECE)
			new_score = minimax(b_copy, depth-1, alpha, beta, True)[1]
			if new_score < value:
				value = new_score
				column = col
			beta = min(beta, value)
			if alpha >= beta:
				break
		return column, value

def minimax2(board, depth, alpha, beta, maximizingPlayer): # whith hiorestic
	valid_locations = get_valid_locations(board)
	is_terminal = is_terminal_node(board)
	if depth == 0 or is_terminal:
		if is_terminal:
			if winning_move(board, AI_PIECE):
				return (None, 100000000000000)
			elif winning_move(board, PLAYER_PIECE):
				return (None, -10000000000000)
			else: # Game is over, no more valid moves
				return (None, 0)
		else: # Depth is zero
			return (None, hiorestic(board))
	if maximizingPlayer:
		value = -math.inf
		column = random.choice(valid_locations)
		for col in valid_locations:
			row = get_next_open_row(board, col)
			b_copy = board.copy()
			drop_piece(b_copy, row, col, AI_PIECE)
			new_score = minimax(b_copy, depth-1, alpha, beta, False)[1]
			if new_score > value:
				value = new_score
				column = col
			alpha = max(alpha, value)
			if alpha >= beta:
				break
		return column, value

	else: # Minimizing player
		value = math.inf
		column = random.choice(valid_locations)
		for col in valid_locations:
			row = get_next_open_row(board, col)
			b_copy = board.copy()
			drop_piece(b_copy, row, col, PLAYER_PIECE)
			new_score = minimax(b_copy, depth-1, alpha, beta, True)[1]
			if new_score < value:
				value = new_score
				column = col
			beta = min(beta, value)
			if alpha >= beta:
				break
		return column, value

def get_valid_locations(board):
	valid_locations = []
	for col in range(COLUMN_COUNT):
		if is_valid_location(board, col):
			valid_locations.append(col)
	return valid_locations


def evaluate_window(window, piece):
	score = 0
	opp_piece = PLAYER_PIECE
	if piece == PLAYER_PIECE:
		opp_piece = AI_PIECE

	if window.count(piece) == 4:
		score += 100
	elif window.count(piece) == 3 and window.count(EMPTY) == 1:
		score += 5
	elif window.count(piece) == 2 and window.count(EMPTY) == 2:
		score += 2

	if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
		score -= 4

	return score

def score_position(board, piece):
	score = 0

	## Score center column
	center_array = [int(i) for i in list(board[:, COLUMN_COUNT//2])]
	center_count = center_array.count(piece)
	score += center_count * 3

	## Score Horizontal
	for r in range(ROW_COUNT):
		row_array = [int(i) for i in list(board[r,:])]
		for c in range(COLUMN_COUNT-3):
			window = row_array[c:c+WINDOW_LENGTH]
			score += evaluate_window(window, piece)

	## Score Vertical
	for c in range(COLUMN_COUNT):
		col_array = [int(i) for i in list(board[:,c])]
		for r in range(ROW_COUNT-3):
			window = col_array[r:r+WINDOW_LENGTH]
			score += evaluate_window(window, piece)

	## Score posiive sloped diagonal
	for r in range(ROW_COUNT-3):
		for c in range(COLUMN_COUNT-3):
			window = [board[r+i][c+i] for i in range(WINDOW_LENGTH)]
			score += evaluate_window(window, piece)

	for r in range(ROW_COUNT-3):
		for c in range(COLUMN_COUNT-3):
			window = [board[r+3-i][c+i] for i in range(WINDOW_LENGTH)]
			score += evaluate_window(window, piece)

	return score

def is_terminal_node(board):
	return winning_move(board, PLAYER_PIECE) or winning_move(board, AI_PIECE) or len(get_valid_locations(board)) == 0

