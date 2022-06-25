from variables import *
from simplelib import *

def user(board,myStone):
  score = [[0 for j in range(BOARDSIZE)] for i in range(BOARDSIZE)]
  for i in range(BOARDSIZE):
    for j in range(BOARDSIZE):
      if board[i][j] is EMPTY:
        board[i][j] = myStone
        '''
        left blank to you
        '''
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
  print(maxi, maxj, max_score)
  return maxi, maxj
