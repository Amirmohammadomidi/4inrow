import math

def hirestic(column , matris):
    '''return Score'''
    test_matris = matris.copy()
    def get_i_j(column  , matris):
        for r in range(6):    # for every row in a given column
            if matris[r][column] == 0: # return the first row that is no yet filled
                return [ r , column ]   #return [i , j]

    def halthaie_bord_player(i , j , matris , player):

        def chek_value(i , j):
            if i in [0, 1, 2 , 3 , 4, 5 ] and j in [0 ,1 ,2 ,3 ,4 ,5 , 6]:
                return True
            else:
                return False

        def halathaie_bord(tedad_khaneha):
            if tedad_khaneha >= 4 :
                return tedad_khaneha - 4 + 1
            else:
                return 0

        def check_row(i, j , matris , player):
            temp = 1
            for m in range(1 , 4):
                if chek_value(i  , j+m):
                    if matris[i][j+m] == player or matris[i][j+m] == 0:
                        temp = temp + 1
                    else:
                        break
                else:
                    break

            for m in range(1 , 4):
                if chek_value(i  , j-m):
                    if matris[i ][j- m] == player or matris[i][j- m] == 0:
                        temp = temp + 1
                    else:
                        break
                else:
                    break
            return halathaie_bord(temp)

        def check_column(i, j , matris , player):
            temp = 1
            for m in range(1 , 4):
                if chek_value(i+m  , j):
                    if matris[i+m][j] == player or matris[i+m][j] == 0:
                        temp = temp + 1
                    else:
                        break
                else:
                    break

            for m in range(1 , 4):
                if chek_value(i-m  , j-m):
                    if matris[i-m][j] == player or matris[i-m][j] == 0:
                        temp = temp + 1
                    else:
                        break
                else:
                    break
            return halathaie_bord(temp)

        def check_movarabchap(i, j , matris  , player):
            temp = 1 
            for m in range(1 , 4):
                if chek_value(i+m  , j-m):
                    if matris[i+m][j-m] == player or matris[i+m][j-m] == 0:
                        temp = temp + 1
                    else:
                        break
                else:
                    break

            for m in range(1 , 4):
                if chek_value(i-m  , j+m):
                    if matris[i-m][j + m ] == player or matris[i-m][j + m] == 0:
                        temp = temp + 1
                    else:
                        break
                else:
                    break
            return halathaie_bord(temp)

        def check_movarabrast(i, j , matris , player):
            temp = 1
            for m in range(1 , 4):
                if chek_value(i+m  , j+m):
                    if matris[i+m][j+m] == player or matris[i+m][j+m] == 0:
                        temp = temp + 1
                    else:
                        break
                else:
                    break

            for m in range(1 , 4):
                if chek_value(i-m  , j-m):
                    if matris[i-m][j -m ] == player or matris[i-m][j - m] == 0:
                        temp = temp + 1
                    else:
                        break
                else:
                    break
            return halathaie_bord(temp)
        return check_row(i , j , matris , player) + check_column(i , j , matris , player) + check_movarabrast(i, j , matris , player) + check_movarabchap(i , j , matris , player) 
 
    i_j = get_i_j(column , matris)
    
    test_matris[i_j[0]][column] = 2
    if win(test_matris , piece=2):
        return math.inf
    else:
        test_matris[i_j[0]][column] = 0

    test_matris[i_j[0]][column] = 1
    if win(test_matris , piece=1):
        return 30000 #big number
    else:
        test_matris[i_j[0]][column] = 0

    test_matris[i_j[0]][column] = 2
    test_matris[i_j[0]+1][column] = 1
    if win(test_matris, piece=1):
        return -30000 #not big number
    else:
        test_matris[i_j[0]][column] = 0
        test_matris[i_j[0]+1][column] = 0

    score = halthaie_bord_player(i_j[0] , i_j[1] , matris , player=2) + halthaie_bord_player(i_j[0] , i_j[1] , matris , player=1)
    return score






    
