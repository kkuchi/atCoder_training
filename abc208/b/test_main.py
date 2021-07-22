import subprocess
from os.path import abspath, dirname

dirpath = dirname(abspath(__file__))

def test_main():
    for i in range(1, 4):
        test = subprocess.run(f'python {dirpath}/main.py < {i}.txt', stdout=subprocess.PIPE)

test_main()