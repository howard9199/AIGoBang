import random
import sys
import re
sys.path.append(f'{sys.path[0]}/..')
from simplelib import *
from variables import *

def user (board, myStone):
    i, j = random.randint(0,14), random.randint(0,14)
    while board[i][j] != EMPTY :
        i, j = random.randint(0,14), random.randint(0,14)
    return i, j


def main():
  r = re.compile(r"[^, 0-9-]")
  raw_data = input()
  raw_data = r.sub("",raw_data)
  user_list = [int(coord) for coord in raw_data.split(', ')]
  input_board = [[]] * 15
  for row in range(15):
    input_board[row] = [0] * 15
  for i in range(15):
    for j in range(15):
      input_board[i][j] = user_list[i*15+j]

  input_mystone = user_list[225]
  i, j = user(input_board,input_mystone)
  print(i,j)

if __name__ == '__main__':
    main()
