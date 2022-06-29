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

        with open(f'{setting}', 'r') as sFile:
            datas = sFile.readlines()
            for i, data in enumerate(datas):
                if data[:4] == 'mode':
                    datas[i] = f'mode = 3\n'
                elif data[:11] == 'team_a_path':
                    datas[i] = f'team_a_path = \'{dirName}/{f1}\'\n'
                elif data[:11] == 'team_b_path':
                    datas[i] = f'team_b_path = \'{dirName}/{f2}\'\n'
                elif data[:10] == 'time_delay':
                    datas[i] = f'time_delay = 500\n'
                elif data[:9] == 'set_delay':
                    datas[i] = f'set_delay = 2000\n'
                elif data[:14] == 'sound_activate':
                    datas[i] = f'sound_activate = False\n'
            sFile.close()

            sFile = open(f'{setting}', 'w')
            sFile.writelines(datas)
            sFile.close()

            os.system(f'python3 main.py')
