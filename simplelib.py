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