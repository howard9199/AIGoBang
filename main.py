from game_set import *
from queue import Empty
import pygame
import time
import random
import copy
print(pygame.ver)

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
score_font = pygame.font.SysFont('Comic Sans MS', 100)
step_font = pygame.font.SysFont('Comic Sans MS', 20)
screen = pygame.display.set_mode((840,640))

 
EMPTY = 0
BLACK = 1
WHITE = 2
 
black_color = [0, 0, 0]

white_color = [255, 255, 255]


# scoreboard
a_team_color = [247, 206, 92]
b_team_color = [247, 206, 92]
losser_color = [202, 203, 207]
winner_color = [110, 250, 95]

 

class RenjuBoard(object):
 
    def __init__(self):
        # self._board = board = [[EMPTY] * 15 for _ in range(15)]
        # board 15*15
        self._board = [[]] * 15
        self.team_score = [0] * 2
        self.team_name = ["team"] * 2
        self.team_step = [0] * 2
        self.one_step = [0] * 2
        self.black_team = 0
        self.reset(0)

    def reset(self, numStone):
        self.one_step[0] = 0
        self.one_step[1] = 0
        for row in range(len(self._board)):
            self._board[row] = [EMPTY] * 15
        for i in range(numStone):
            r, c = random.randint(3, 15-4), random.randint(3, 15-4)
            while not self.move(r, c, i%2 == 0):
                r, c = random.randint(3, 15-4), random.randint(3, 15-4)

    def reset_to(self, board):
        self.one_step[0] = 0
        self.one_step[1] = 0
        self._board = board
        

    def switch(self):
        self.black_team = not self.black_team

    def isValid(self, row, col):
        if row < 0 or row >= 15:
            return False
        if col < 0 or col >= 15:
            return False
        return self._board[row][col] is EMPTY

    def move(self, row, col, is_black):
        if self.isValid(row, col):
            self._board[row][col] = BLACK if is_black else WHITE
            return True
        return False

    def gain_point(self, win_team):
        if win_team == BLACK:
            self.team_score[self.black_team] += 1
            self.team_step[self.black_team] += self.one_step[self.black_team]
        else:
            self.team_score[not self.black_team] += 1
            self.team_step[not self.black_team] += self.one_step[not self.black_team]

    def draw(self, screen, winner):
        for h in range(1, 16):
            pygame.draw.line(screen, black_color,
                             [40, h * 40], [600, h * 40], 1)
            pygame.draw.line(screen, black_color,
                             [h * 40,40], [h * 40, 600], 1)
        pygame.draw.rect(screen, black_color, [36, 36, 568, 568], 3)
 
        pygame.draw.circle(screen, black_color, [320, 320], 5, 0)
        pygame.draw.circle(screen, black_color, [160, 160], 3, 0)
        pygame.draw.circle(screen, black_color, [160, 480], 3, 0)
        pygame.draw.circle(screen, black_color, [480, 160], 3, 0)
        pygame.draw.circle(screen, black_color, [480, 480], 3, 0)
        for row in range(len(self._board)):
            for col in range(len(self._board[row])):
                if self._board[row][col] != EMPTY:
                    ccolor = black_color \
                        if self._board[row][col] == BLACK else white_color
                    pos = [40 * (col + 1), 40 * (row + 1)]
                    pygame.draw.circle(screen, ccolor, pos, 18, 0)
        # draw scoreboard
        if winner == 0:
            recta_filled = pygame.Rect(630, 20, 180, 180)
            pygame.draw.rect(screen, a_team_color, recta_filled) 
            rectb_filled = pygame.Rect(630, 420, 180, 180)
            pygame.draw.rect(screen, b_team_color, rectb_filled)
        elif winner == 1:
            recta_filled = pygame.Rect(630, 20, 180, 180)
            pygame.draw.rect(screen, winner_color, recta_filled) 
            rectb_filled = pygame.Rect(630, 420, 180, 180)
            pygame.draw.rect(screen, losser_color, rectb_filled)
        elif winner == 2:
            recta_filled = pygame.Rect(630, 20, 180, 180)
            pygame.draw.rect(screen, losser_color, recta_filled) 
            rectb_filled = pygame.Rect(630, 420, 180, 180)
            pygame.draw.rect(screen, winner_color, rectb_filled)        

        text_a_name = my_font.render(self.team_name[0], False, (0, 0, 0))
        screen.blit(text_a_name, (650,210))
        text_a_score = score_font.render(str(self.team_score[0]), False, (0, 0, 0))
        screen.blit(text_a_score, (680,50))
        text_b_name = my_font.render(self.team_name[1], False, (0, 0, 0))
        screen.blit(text_b_name, (650,370))
        text_b_score = score_font.render(str(self.team_score[1]), False, (0, 0, 0))
        screen.blit(text_b_score, (680,480))

        #team_a chess
        ccolor = black_color \
            if self.black_team == 0 else white_color
        pygame.draw.circle(screen, ccolor, [780,230], 25, 0)
        #team_b chess
        ccolor = black_color \
            if self.black_team == 1 else white_color
        pygame.draw.circle(screen, ccolor, [780,390], 25, 0)
        #team_a step info
        text_a_score = step_font.render("Win Step:"+str(self.team_step[0]), False, (0, 0, 0))
        screen.blit(text_a_score, (680,20))
        #team_b step info
        text_b_score = step_font.render("Win Step:"+str(self.team_step[1]), False, (0, 0, 0))
        screen.blit(text_b_score, (680,420))



def is_win(board):
    for n in range(15):

        flag = 0

        for b in board._board:
            if b[n] == 1:
                flag += 1
                if flag == 5:
                    text_surface = my_font.render('Black Win', False, (0, 0, 0),(0, 255, 0))
                    screen.blit(text_surface, (255,300))
                    pygame.display.flip()
                    print('黑棋勝')
                    return BLACK
            else:
                flag = 0
 
        flag = 0
        for b in board._board:
            if b[n] == 2:
                flag += 1
                if flag == 5:
                    text_surface = my_font.render('White Win', False, (0, 0, 0),(0, 255, 0))
                    screen.blit(text_surface, (255,300))
                    pygame.display.flip()
                    print('白棋勝')
                    return WHITE
            else:
                flag = 0
 
        flag = 0
        for b in board._board[n]:
            if b == 1:
                flag += 1
                if flag == 5:
                    text_surface = my_font.render('Black Win', False, (0, 0, 0),(0, 255, 0))
                    screen.blit(text_surface, (255,300))
                    pygame.display.flip()
                    print('黑棋勝')
                    return BLACK
            else:
                flag = 0
 
        flag = 0
        for b in board._board[n]:
            if b == 2:
                flag += 1
                if flag == 5:
                    text_surface = my_font.render('White Win', False, (0, 0, 0),(0, 255, 0))
                    screen.blit(text_surface, (255,300))
                    pygame.display.flip()
                    print('白棋勝')
                    return WHITE
            else:
                flag = 0
 
        for x in range(4, 25):
            flag = 0
            for i,b in enumerate(board._board):
                if 14 >= x - i >= 0 and b[x - i] == 1:
                    flag += 1
                    if flag == 5:
                        text_surface = my_font.render('Black Win', False, (0, 0, 0),(0, 255, 0))
                        screen.blit(text_surface, (255,300))
                        pygame.display.flip()
                        print('黑棋勝')
                        return BLACK
                else:
                    flag = 0
 
        for x in range(4, 25):
            flag = 0
            for i,b in enumerate(board._board):
                if 14 >= x - i >= 0 and b[x - i] == 2:
                    flag += 1
                    if flag == 5:
                        text_surface = my_font.render('White Win', False, (0, 0, 0),(0, 255, 0))
                        screen.blit(text_surface, (255,300))
                        pygame.display.flip()
                        print('白棋勝')
                        return WHITE
                else:
                    flag = 0
 
        for x in range(11, -11, -1):
            flag = 0
            for i,b in enumerate(board._board):
                if 0 <= x + i <= 14 and b[x + i] == 1:
                    flag += 1
                    if flag == 5:
                        text_surface = my_font.render('Black Win', False, (0, 0, 0),(0, 255, 0))
                        screen.blit(text_surface, (255,300))
                        pygame.display.flip()
                        print('黑棋勝')
                        return BLACK
                else:
                    flag = 0
 
        for x in range(11, -11, -1):
            flag = 0
            for i,b in enumerate(board._board):
                if 0 <= x + i <= 14 and b[x + i] == 2:
                    flag += 1
                    if flag == 5:
                        text_surface = my_font.render('White Win', False, (0, 0, 0),(0, 255, 0))
                        screen.blit(text_surface, (255,300))
                        pygame.display.flip()
                        print('白棋勝')
                        return WHITE
                else:
                    flag = 0
 
    return EMPTY
 
 
def main():
    team_a_name = team_a
    team_b_name = team_b
    if mode == 2:
        team_b_name = team_a_name
        print("測試模式說明：")
        print("每一步棋皆等待玩家操作，若按下空白鍵，則由程式下出下一手，若用滑鼠點按則可直接下下一手棋。")
    modA = __import__(team_a_name)
    modB = __import__(team_b_name)

    board = RenjuBoard()
    board.team_name[0] = team_a_name
    board.team_name[1] = team_b_name

    # step count

    pygame.init()
    pygame.display.set_caption('GoBang')

    screen.fill([230, 169, 37])
    board.draw(screen,EMPTY) 
    pygame.display.flip()

    total_set = 1
    if(mode == 3):
        total_set = 4

    set_count = 0

    if mode == 1 or mode == 3:
        while set_count < total_set:  
            running = True
            is_black = True
            if set_count % 2 == 0:
                board.reset( 2 * (set_count//2) )
                prevInit = copy.deepcopy(board._board)
            else:
                board.reset_to(prevInit)
            board.switch()
            
            screen.fill([230, 169, 37])
            board.draw(screen,EMPTY)
            pygame.display.flip()
            pygame.time.delay(2000)
            
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return None

                pygame.time.delay(time_delay)

                color = BLACK if is_black else WHITE
                team = board.black_team if is_black else not board.black_team
                if team == 0:
                    row,col = modA.user(board._board,color)
                else:
                    row,col = modB.user(board._board,color)
                print(row,col)
                if board.move(row, col, is_black):
                    board.one_step[team] += 1

                is_black = not is_black

                screen.fill([230, 169, 37])
                board.draw(screen,EMPTY)
                pygame.display.flip()

                status = is_win(board)
                if status > 0:
                    pygame.time.delay(2000)
                    board.gain_point(status)
                    running = False

            set_count += 1
            if mode == 3 and total_set == 4 and set_count == total_set and board.team_score[0] == board.team_score[1] and board.team_step[0] == board.team_step[1]:
                total_set += 2

    elif mode == 2:
        running = True
        is_black = True
        board.reset(0)
        while running:
            for event in pygame.event.get():

                row, col = -1, -1
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return None

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    if is_black:
                        row,col = modA.user(board._board,1)
                    else:
                        row,col = modB.user(board._board,2)
                    print(f'row: {row}, col: {col}')

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    row = round((y - 40) / 40)
                    col = round((x - 40) / 40)
                else:
                    continue
                
                if not board.move(row, col, is_black):
                    print(row, col)
                    print("Invalid index.")
                    exit()
                
                is_black = not is_black
                screen.fill([230, 169, 37])
                board.draw(screen,EMPTY)
                pygame.display.flip()
                if is_win(board):
                    pygame.time.wait(3000)
                    running = False

    screen.fill([230, 169, 37])
    board.draw(screen,EMPTY)
    pygame.display.flip()

    if(board.team_score[0] > board.team_score[1]):
        board.draw(screen,1)
    elif(board.team_score[0] < board.team_score[1]):
        board.draw(screen,2)
    elif(board.team_step[0] < board.team_step[1]):
        board.draw(screen,1)
    elif(board.team_step[0] > board.team_step[1]):
        board.draw(screen,2)
    else:
        board.draw(screen,0)
    pygame.display.flip()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__ == '__main__':
    main()
