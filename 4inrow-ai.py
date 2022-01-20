import math

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

    if win(matris , piece=2):
        return math.inf
    elif win(matris , piece=1):
        return -math.inf

    Our_win_modes = win_modes(matris , piece=2)
    oponent_win_modes = win_modes(matris , piece=1)
    score = Our_win_modes - oponent_win_modes 
    return score

