'''
1. single round
2. test mode
    測試模式說明：每一步棋皆等待玩家操作，若按下空白鍵，則由程式下出下一手，若用滑鼠點按則可直接下下一手棋。
3. competition mode
'''
mode = 2

'''
requirement:
1. both
2. team_a only
3. both

請輸入你的程式的路徑，其中檔名的部分會成為隊名
'''
team_a_path = 'template.py'
team_b_path = 'template.py'

'''
time delay between each step (unit: ms)
每顆棋之間的延遲時間，單位為毫秒
'''
time_delay = 500

'''
time delay between each set (unit: ms)
每局之間的延遲時間，單位為毫秒
'''
set_delay = 2000

'''
some reality sound effect
擬真音效，我知道你用學校電腦聽不到
'''
sound_activate = False
