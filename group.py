from time import perf_counter
from subprocess import check_output
import subprocess
import os
import sys

dirName = 'programs'
files = os.listdir(dirName)

board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

times = [0] * len(files)

for i, name in enumerate(files):
    start = perf_counter()
    try:
        result = check_output(f'python3 {sys.path[0]}/{dirName}/{name}', shell=True, input= str(str(board)+', 1'),encoding='ascii',timeout=3).split()
    except subprocess.TimeoutExpired:
        print(f'team \'{name}\': TIME LIMIT EXCEEDED(超時)')
        del files[i]
        del times[i]
        i -= 1
        continue
    except Exception as err:
        print(err)
        exit()
    end = perf_counter()
    times[i] = end-start

#print(files)
#print(times)

times, files = zip(*sorted(zip(times, files)))
#print(files)
#print(times)

groups = (len(files)-1) // 4 + 1
for g in range(groups):
    os.system(f'mkdir -p group{g}')
    os.system(f'rm -f group{g}/*')

for i, name in enumerate(files):
    os.system(f'cp {sys.path[0]}/{dirName}/{name} group{i%groups}/')
