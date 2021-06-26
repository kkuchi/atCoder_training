import itertools

n = int(input())

T = []

for i in range(n):
    mode, l, r = map(int, input().split())
    # mode: 0→[], 1→()
    if mode == 1:
        ll, rr = 0, 0
    elif mode == 2:
        ll, rr = 0, 1
    elif mode == 3:
        ll, rr = 1, 0
    else:
        ll, rr = 1, 1
    T += [[ll, rr, l, r]]

res = 0

for i,v in itertools.combinations(range(n), 2):
    x, y = T[i], T[v]
    xl, yl = x[2], y[2]
    xr, yr = x[3], y[3]

    if xl == yl:
        if x[0] == y[0] == 0:
            left_symbol = 0
        else:
            left_symbol = 1
    elif xl > yl:
        left_symbol = x[0]
    else:
        left_symbol = y[0]
    
    if xr == yr:
        if x[1] == y[1] == 0:
            right_symbol = 0
        else:
            right_symbol = 1
    elif xr < yr:
        right_symbol = x[1]
    else:
        right_symbol = y[1]
    
    left, right = max(xl, yl), min(xr, yr)

    if left < right:
        res += 1
    elif left == right:
        if left_symbol == right_symbol == 0:
            res += 1

print(res)
