from os import getcwd, listdir
from subprocess import run as sprun

dirpath = getcwd()
print(dirpath)

# テキストファイルのリスト
files = listdir(dirpath)
print(files)

count = 1
while True:
    check_in = f'in_{count}.txt' 
    if check_in not in files:
        break
    
    check_sp = sprun(['python', 'main.py', f'< {check_in}'])
    
    with open(f'{dirpath}/out_{count}.txt', 'r') as f:
        check_out = f.read()
    
    if check_sp.stdout == check_out:
        print('AC')
    else:
        print('WA')

    count += 1
