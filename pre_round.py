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
        fo = open(f'{setting}', 'w')
        fo.write('mode = 3\n')
        fo.write(f'team_a_path = \'{dirName}/{f1}\'\n')
        fo.write(f'team_b_path = \'{dirName}/{f2}\'\n')
        fo.write('time_delay = 500\n')
        fo.write('set_delay = 2000\n')
        fo.write('sound_activate = False\n')
        fo.close()
        os.system(f'python3 main.py')
