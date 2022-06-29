import sys
sys.path.append(f'{sys.path[0]}/..')
from simplelib import *
from variables import *
import re


# user:
#
# param:
#   board: list[list[int]]
#       board.size == board[0].size == BOARDSIZE
#   myStone: int
#       myStone in [EMPTY, BLACK, WHITE] (0, 1, 2)
# return: row, column
#
# 根據目前的 board，輪到 myStone，回傳要下的(row, col)。
# 整個 user 都可以改，除此之外都不要改

# 定義請看 variables.py
# 輔助函式請看 simplelib.py

def user(board,myStone):

  score = [[0 for j in range(BOARDSIZE)] for i in range(BOARDSIZE)] # score 儲存每個格子的分數

  for i in range(BOARDSIZE):
    for j in range(BOARDSIZE): # 遍例每個格子
      if board[i][j] is EMPTY: # 對空的格子算分
        board[i][j] = myStone # 試著下在這格
        '''
        left blank to you
        '''
        board[i][j] = EMPTY # 試完了，拿起來

  # 取最大分數的格子回傳
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


# DO NOT modify code below!(請絕對不要更改以下程式碼)
# 也可以不用看
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
