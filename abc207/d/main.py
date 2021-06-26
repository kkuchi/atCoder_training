import sys
import numpy as np

def pull_to_zero(s):
    if [0, 0] in s:
        return s
    
    pull_x, pull_y = s[0][0], s[0][1]

    new_s = []
    for x,y in s:
        new_s += [[x-pull_x, y-pull_y]]
    
    return new_s

def pull_to_pos(t, num):
    pull_x, pull_y = t[num][0], t[num][1]

    new_t = []
    for x,y in t:
        new_t += [[x-pull_x, y-pull_y]]
    
    return new_t

def rotate(s, t):
    news = set([tuple(i) for i in s])
    for i in range(360):
        rad = np.deg2rad(i)
        sin = np.sin(rad)
        cos = np.cos(rad)

        new_t = []
        for x,y in t:
            newx = cos*x-sin*y
            newy = sin*x+cos*y
            if newx.is_integer() and newy.is_integer():
                new_t += [(newx, newy)]
            else:
                continue
        check_t = set(new_t)

        for i in news:
            if i not in check_t:
                continue

        return True

    return False

def main():
    source = sys.stdin.read().splitlines()

    n = int(source[0])
    s = [[int(i) for i in row.split()] for row in source[1:n+1]]
    t = [[int(i) for i in row.split()] for row in source[n+1:2*n+1]]

    news = pull_to_zero(s)

    for i in range(n):
        new_t = pull_to_pos(t, i)
        res = rotate(news, new_t)
        if res:
            print('Yes')
            sys.exit()
    
    print('No')

main()