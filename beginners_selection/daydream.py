import re

def sub():
    s = input()

    reg = re.compile('^(dream|dreamer|erase|eraser){1,}$')
    if reg.match(s):
        print('YES')
    else:
        print('NO')


# main()
sub()