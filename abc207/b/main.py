import math

a,b,c,d = map(int, input().split())

if c*d-b == 0:
    print(-1)
else:
    check = a/(c*d-b)

    if check < 0:
        print(-1)
    else:
        print(math.ceil(check))
