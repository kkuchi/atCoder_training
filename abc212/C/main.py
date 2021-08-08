import sys
from bisect import bisect_left


def calc(n, m, a, b):
    b.sort()
    blen = len(b)
    INF = 2 << 60
    ans = INF

    for i in range(n):
        obj = a[i]
        b_index = bisect_left(b, obj)

        check1 = abs(obj - b[b_index-1])

        if b_index == blen:
            check2 = INF
        else:
            check2 = abs(obj - b[b_index])

        res = min(check1, check2)

        if ans > res:
            ans = res
    
    return ans


def main():
    read = sys.stdin.buffer.readline
    spi = lambda x: map(int, x.split())

    n, m = spi(read())
    A = list(spi(read()))
    B = list(spi(read()))

    ans = calc(n, m, A, B)
    print(ans)

main()