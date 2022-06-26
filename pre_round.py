import sys
import os

if len(sys.argv) < 2:
    print("Please enter the directory name")
    exit()

setting = 'game_set.py'
dirName = sys.argv[1]

files = os.listdir(dirName)
counter = 0
for i, f1 in enumerate(files):
    for j in range(i+1, len(files)):
        f2 = files[j]
        counter += 1
        print(f'round {counter}: {f1} vs {f2}')
        os.system(f'echo \'mode = 3\' > {setting}')
        os.system(f'echo \"team_a_path = \'{dirName}/{f1}\'\" >> {setting}')
        os.system(f'echo \"team_b_path = \'{dirName}/{f2}\'\" >> {setting}')
        os.system(f'echo \'time_delay = 500\' >> {setting}')
        os.system(f'echo \'set_delay = 2000\' >> {setting}')
        os.system(f'echo \'sound_activate = False\' >> {setting}')
        os.system(f'python3 main.py')
