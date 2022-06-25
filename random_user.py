from simplelib import *
from variables import *
import random

def user (board, myStone):
    i, j = random.randint(0,14), random.randint(0,14)
    while board[i][j] != EMPTY :
        i, j = random.randint(0,14), random.randint(0,14)
    return i, j
