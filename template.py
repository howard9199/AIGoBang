import sys
sys.path.append(f'{sys.path[0]}/..')
from simplelib import *
from variables import *
import re


def user(board,myStone,remain_time):
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
  print(maxi, maxj, max_score, file=sys.stderr)
  return maxi, maxj


# DO NOT modify code below!
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
  remain_t = user_list[226]
  # print_to_stderr(input_board)
  # print('stone:'+str(input_mystone))
  i, j = user(input_board,input_mystone,remain_t)
  print(i,j)


if __name__ == '__main__':
    main()
