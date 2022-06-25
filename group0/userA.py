import sys
sys.path.append(f'{sys.path[0]}/..')
from simplelib import *
from variables import *
import re

def user(board,myChess):
  score = [[0 for j in range(BOARDSIZE)] for i in range(BOARDSIZE)]
  for i in range(BOARDSIZE):
    for j in range(BOARDSIZE):
      if board[i][j] is EMPTY:
        board[i][j] = myChess
        rowB, colB, ldiaB, rdiaB = countChain(board,myChess)
        maxRepeat = funcMaxRepeat(rowB, colB, ldiaB, rdiaB)
        board[i][j] = 3-myChess
        rowB1, colB1, ldiaB1, rdiaB1 = countChain(board,3-myChess)
        maxRepeat1 = funcMaxRepeat(rowB1, colB1, ldiaB1, rdiaB1)
        score[i][j] = pow(maxRepeat[i][j],3)+pow(maxRepeat1[i][j],3)
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

def print_to_stderr(*a):
 
    # Here a is the array holding the objects
    # passed as the argument of the function
    print(*a, file = sys.stderr)

def main():
  r = re.compile(r"[^, 0-9-]")
  raw_data = input()
  raw_data = r.sub("",raw_data)
  # print(raw_data)
  user_list = [int(coord) for coord in raw_data.split(', ')]
  # print(user_list)
  input_board = [[]] * 15
  for row in range(15):
    input_board[row] = [0] * 15
  for i in range(15):
    for j in range(15):
      input_board[i][j] = user_list[i*15+j]

  input_mystone = user_list[225]
  # print_to_stderr(input_board)
  # print('stone:'+str(input_mystone))
  i, j = user(input_board,input_mystone)
  print(i,j)

if __name__ == '__main__':
    main()
