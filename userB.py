from variables import *
from simplelib import *
def user(board,myChess):
  score = [[0 for j in range(BOARDSIZE)] for i in range(BOARDSIZE)]
  for i in range(BOARDSIZE):
    for j in range(BOARDSIZE):
      if board[i][j] is EMPTY:
        board[i][j] = myChess
        rowB, colB, ldiaB, rdiaB = countChain(board,myChess)
        maxRepeat = funcMaxRepeat(rowB, colB, ldiaB, rdiaB)
        score[i][j] = maxRepeat[i][j]
        board[i][j] = EMPTY
  maxi = 0
  maxj = 0
  max_score = -1
  for i in range(BOARDSIZE):
    for j in range(BOARDSIZE):
      if score[i][j] > max_score:
        max_score = score[i][j]
        maxi = i
        maxj = j
  return maxi, maxj

def valid(a, b):
  return (a >= 0 and a < BOARDSIZE) and (b >= 0 and b < BOARDSIZE)

def funcMaxRepeat(rowB, colB, ldiaB, rdiaB):
  maxRepeat = [[0 for j in range(BOARDSIZE)] for i in range(BOARDSIZE)]
  for i in range(BOARDSIZE):
    for j in range(BOARDSIZE):
      maxRepeat[i][j] = max(maxRepeat[i][j], rowB[i][j])
      maxRepeat[i][j] = max(maxRepeat[i][j], colB[i][j])
      maxRepeat[i][j] = max(maxRepeat[i][j], ldiaB[i][j])
      maxRepeat[i][j] = max(maxRepeat[i][j], rdiaB[i][j])
  return maxRepeat