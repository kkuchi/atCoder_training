#!/usr/bin/env python3
import sys
import itertools

def sub(n, k):
    return itertools.product(range(n-k+1), repeat=2)

iter_ac = itertools.accumulate

def calc2(bi_height, n):
    # iter_acで行ごとの累積和を求め、forで縦の累積和
    bi_height_s = [list(iter_ac(row)) for row in bi_height]
    for y in range(1, n+1):
        for x in range(n+1):
            top = bi_height_s[y-1][x]
            bi_height_s[y][x] += top
    
    return bi_height_s

def main():
    source = sys.stdin.read().splitlines()
    n, k = map(int, source[0].split())
    height_flat = [int(i) for i in ' '.join(source[1:]).split()]
    height = [height_flat[i*n:(i+1)*n] for i in range(n)]

    half = k ** 2 // 2 + 1

    ok = max(height_flat)
    ng = 0

    while ok - ng > 1:
        # 個数の判定
        check = (ok + ng) // 2
        flag = False
        # heightを1と0に。最初の行と列に0を入れる
        bi_height = [[0]+[1 if a > check else 0 for a in row] for row in height]
        bi_height = [[0]*(n+1)] + bi_height
        
        bi_height_s = calc2(bi_height, n)
        
        for i, j in sub(n,k):
            target = bi_height_s[i+k][j+k] \
                        - bi_height_s[i+k][j] \
                        - bi_height_s[i][j+k] \
                        + bi_height_s[i][j]
            if target < half:
                flag = True
                break

        if flag:
            ok = check
        else:
            ng = check

    print(ok)

if __name__ == '__main__':
    main()
