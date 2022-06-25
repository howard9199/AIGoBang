from variables import *
import copy

def countChain (board, stone) :
#def countChain( board : list[list[int]], stone : int = BLACK ) -> tuple[ list[list[int]], list[list[int]], list[list[int]], list[list[int]] ] :
	
	isYours = [ [ int(grid == stone) for grid in row ] for row in board ]	
	rowChain = isYours
	colChain = copy.deepcopy(isYours)
	ldiaChain = copy.deepcopy(isYours)
	rdiaChain = copy.deepcopy(isYours)

	for i in range(BOARDSIZE) :
		for j in range(BOARDSIZE) :
			if (j != 0 and rowChain[i][j]):
				rowChain[i][j] = rowChain[i][j-1] + 1
			if (i != 0 and colChain[i][j]):
				colChain[i][j] = colChain[i-1][j] + 1
			if (i != 0 and j != 0 and ldiaChain[i][j]):
				ldiaChain[i][j] = ldiaChain[i-1][j-1] + 1;
			if (i != 0 and j != BOARDSIZE-1 and rdiaChain[i][j]) :
				rdiaChain[i][j] = rdiaChain[i-1][j+1] + 1
				
	for i in range(BOARDSIZE-1,-1,-1) :
		for j in range(BOARDSIZE-1,-1,-1) :
			if (j != BOARDSIZE-1 and rowChain[i][j] and rowChain[i][j+1]) :
				rowChain[i][j] = rowChain[i][j+1] 
			if (i != BOARDSIZE-1 and rowChain[i][j] and rowChain[i+1][j]) :
				colChain[i][j] = colChain[i+1][j]
			if (i != BOARDSIZE-1 and j != BOARDSIZE-1 and ldiaChain[i][j] and ldiaChain[i+1][j+1]) :
				ldiaChain[i][j] = ldiaChain[i+1][j+1];
			if (i != BOARDSIZE-1 and j != 0 and rdiaChain[i][j] and rdiaChain[i+1][j-1]) :
				rdiaChain[i][j] = rdiaChain[i+1][j-1]
	return rowChain, colChain, ldiaChain, rdiaChain


def peek (board, i , j, stone):
#def peek( board:list[list[int]], i:int, j:int, stone:int ) -> list[list[int, bool]]

    if i < 0 or i >= BOARDSIZE or j < 0 or j >= BOARDSIZE:
        print("Invalid index to peek")
        return None

    ret = [[0, False] for _ in range(8)]

    for k in range(8):

        y = i
        x = j

        if k == 2 or k == 6 : # horizontal
            delY = 0
        else :
            delY = 1 if k > 2 and k < 6 else -1

        if k == 0 or k == 4 : # vertical
            delX = 0
        else :
            delX = 1 if k > 0 and k < 4 else -1

        while True:
            y += delY
            x += delX
            if y < 0 or y >= BOARDSIZE : break
            if x < 0 or x >= BOARDSIZE : break
            if board[y][x] != stone : break
            ret[k][0] += 1

        if y < 0 or y >= BOARDSIZE : continue
        if x < 0 or x >= BOARDSIZE : continue
        ret[k][1] = board[y][x] == EMPTY

    return ret
