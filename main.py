'''
to do:
檢查是否下錯
改自
https://blog.csdn.net/bigzql/article/details/112386871?fbclid=IwAR108kiVP4oCyjHeDwhgSKEbbmRjEIo4Z1AgULEmLIsujG2TZhG_ebi9BtY
'''
from queue import Empty
import pygame
import time
# 导入pygame模块
print(pygame.ver)
# 检查pygame的版本，检查pygame有没有导入成功

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
score_font = pygame.font.SysFont('Comic Sans MS', 100)
screen = pygame.display.set_mode((840,640))

 
EMPTY = 0
BLACK = 1
WHITE = 2
# 定义三个常量函数，用来表示白棋，黑棋，以及 空
 
black_color = [0, 0, 0]
# 定义黑色（黑棋用，画棋盘）
white_color = [255, 255, 255]
# 定义白色（白棋用）

# scoreboard
a_team_color = [247, 206, 92]
b_team_color = [247, 206, 92]

 
# 定义棋盘这个类
class RenjuBoard(object):
 
    def __init__(self):
        # self._board = board = [[EMPTY] * 15 for _ in range(15)]
        # 将棋盘每一个交叉点都看作列表的一个元素位，一共有15*15共225个元素
        self._board = [[]] * 15
        self.team_score = [0] * 2
        self.team_name = ["team"] * 2
        self.black_team = 0
        self.reset()
    #重置棋盘
    def reset(self):
        for row in range(len(self._board)):
            self._board[row] = [EMPTY] * 15
    #下一局
    def switch(self):
        self.black_team = not self.black_team
    #定义棋盘上的下棋函数，row表示行，col表示列，is_black表示判断当前点位该下黑棋，还是白棋
    def move(self, row, col, is_black):
        if self._board[row][col] == EMPTY:
            self._board[row][col] = BLACK if is_black else WHITE
            return True
        return False
    # 結算分數
    def gain_point(self, win_team):
        if win_team == BLACK:
            self.team_score[self.black_team] += 1
        else:
            self.team_score[not self.black_team] += 1
    # 给棋盘定义一个函数将自己在screen上面画出来，使用pygame.draw()函数。并且顺便将下了的棋子也画出来
    def draw(self, screen):
        for h in range(1, 16):
            pygame.draw.line(screen, black_color,
                             [40, h * 40], [600, h * 40], 1)
            pygame.draw.line(screen, black_color,
                             [h * 40,40], [h * 40, 600], 1)
        # 给棋盘加一个外框，使美观
        pygame.draw.rect(screen, black_color, [36, 36, 568, 568], 3)
 
        # 在棋盘上标出，天元以及另外4个特殊点位
        pygame.draw.circle(screen, black_color, [320, 320], 5, 0)
        pygame.draw.circle(screen, black_color, [160, 160], 3, 0)
        pygame.draw.circle(screen, black_color, [160, 480], 3, 0)
        pygame.draw.circle(screen, black_color, [480, 160], 3, 0)
        pygame.draw.circle(screen, black_color, [480, 480], 3, 0)
        #做2次for循环取得棋盘上所有交叉点的坐标
        for row in range(len(self._board)):
            for col in range(len(self._board[row])):
                # 将下在棋盘上的棋子画出来
                if self._board[row][col] != EMPTY:
                    ccolor = black_color \
                        if self._board[row][col] == BLACK else white_color
                    # 取得这个交叉点下的棋子的颜色，并将棋子画出来
                    pos = [40 * (col + 1), 40 * (row + 1)]
                    # 画出棋子
                    pygame.draw.circle(screen, ccolor, pos, 18, 0)
        # draw scoreboard
        recta_filled = pygame.Rect(630, 20, 180, 180)
        pygame.draw.rect(screen, a_team_color, recta_filled) 
        rectb_filled = pygame.Rect(630, 420, 180, 180)
        pygame.draw.rect(screen, b_team_color, rectb_filled)

        text_a_name = my_font.render(self.team_name[0], False, (0, 0, 0))
        screen.blit(text_a_name, (650,210))
        text_a_score = score_font.render(str(self.team_score[0]), False, (0, 0, 0))
        screen.blit(text_a_score, (680,50))

        #team_a chess
        ccolor = black_color \
            if self.black_team == 0 else white_color
        pygame.draw.circle(screen, ccolor, [780,230], 25, 0)
        #team_b chess
        ccolor = black_color \
            if self.black_team == 1 else white_color
        pygame.draw.circle(screen, ccolor, [780,400], 25, 0)



 
# 定义函数，传入当前棋盘上的棋子列表，输出结果，不管黑棋白棋胜，都是传回False，未出结果则为True
def is_win(board):
    for n in range(15):
        # 判断垂直方向胜利
        flag = 0
        # flag是一个标签，表示是否有连续以上五个相同颜色的棋子
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
            # else表示此时没有连续相同的棋子，标签flag重置为0
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
 
        # 判断水平方向胜利
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
 
        # 判断正斜方向胜利
 
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
 
        #判断反斜方向胜利
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
    team_a_name = input('Enter team A:')
    team_b_name = input('Enter team B:')
    modA = __import__(team_a_name)
    modB = __import__(team_b_name)
    print('1) 機vs機')
    print('2) 測試模式')
    print('3) competition mode')
    mode = 1#int(input('Enter game mode:'))
    # 创建棋盘对象
    board = RenjuBoard()
    board.team_name[0] = team_a_name
    board.team_name[1] = team_b_name

    # 用于判断是下黑棋还是白棋
    is_black = True
    # pygame初始化函数，固定写法
    pygame.init()
    pygame.display.set_caption('GoBang') # 改标题
    # pygame.display.set_mode()表示建立个窗口，左上角为坐标原点，往右为x正向，往下为y轴正向
    # screen = pygame.display.set_mode((640,640))
    # 给窗口填充颜色，颜色用三原色数字列表表示
    screen.fill([125,95,24])
    board.draw(screen)  # 给棋盘类发命令，调用draw()函数将棋盘画出来
    pygame.display.flip()  # 刷新窗口显示

    total_set = 1
    if(mode == 3):
        total_set = 4
    # while 主循环的标签，以便跳出循环
    if mode == 1 or mode == 3:
        while total_set:
            running = True
            board.reset()
            while running:
            # 遍历建立窗口后发生的所有事件，固定写法
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                if is_black:
                    row,col = modA.user(board._board,1)
                    print(row,col)
                    if board.move(row, col, is_black):
                        is_black = not is_black
                        screen.fill([125, 95, 24])
                        board.draw(screen)
                        pygame.display.flip()
                            # 调用判断胜负函数
                        status = is_win(board)
                        if status > 0:
                            board.gain_point(status)
                            running = False
                    pygame.time.delay(100)            
                else:
                    row,col = modB.user(board._board,2)
                    print(row,col)
                    if board.move(row, col, is_black):
                        is_black = not is_black
                        screen.fill([125, 95, 24])
                        board.draw(screen)
                        pygame.display.flip()
                        # 调用判断胜负函数
                        status = is_win(board)
                        if status > 0:
                            board.gain_point(status)
                            running = False
                pygame.time.delay(100)   
            total_set -= 1
    screen.fill([125, 95, 24])
    board.draw(screen)
    pygame.display.flip()
    
    pygame.time.delay(1000)
    pygame.quit()
 
 
 
if __name__ == '__main__':
    main()

'''
                for event in pygame.event.get():
                    # 根据事件的类型，进行判断
                    if event.type == pygame.QUIT:
                        running = False
        
                    elif event.type == pygame.KEYUP:
                        pass
                    # pygame.MOUSEBUTTONDOWN表示鼠标的键被按下
                    elif event.type == pygame.MOUSEBUTTONDOWN and \
                            event.button == 1:# button表示鼠标左键
                        if is_black:
                            print("ok")
                            row,col = modA.user(board._board)
                        else:
                            print("ok1")
                            x, y = event.pos  # 拿到鼠标当前在窗口上的位置坐标
                            # 将鼠标的(x, y)窗口坐标，转化换为棋盘上的坐标
                            row = round((y - 40) / 40)     
                            col = round((x - 40) / 40)
                        print(row,col)
                        if board.move(row, col, is_black):
                            is_black = not is_black
                            screen.fill([125, 95, 24])
                            board.draw(screen)
                            pygame.display.flip()
                            # 调用判断胜负函数
                            if not is_win(board):
                                #break
                                running = False
'''