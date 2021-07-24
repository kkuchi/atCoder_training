#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int

def source():
    # 関数
    spi = lambda x: map(int, x.split())
    # 読み
    s = sys.stdin.read().splitlines()
    h, w = spi(s[0])
    grid = s[1:]
    # return
    return h, w, grid


# dp計算
def calc(h, w, grid):
    # h, wに1足してdp配列作成
    dp = [[0 for _ in range(w+1)] for _ in range(h+1)]

    # 最上段と最左列は0なので1から
    for i in range(1, h+1):
        for j in range(1, w+1):
            # 1,1は初期位置なので1
            if i == j == 1:
                dp[i][j] = 1
                continue
            # #は障害物なので0
            elif grid[i-1][j-1] == "#":
                continue
            # その他の場合は左と上を足す
            else:
                left = dp[i][j-1]
                top = dp[i-1][j]
                dp[i][j] = left+top
    
    # 余りにしてreturn
    res = dp[h][w] % MOD
    return res

def main():
    h, w, grid = source()
    
    ans = calc(h, w, grid)

    print(ans)

if __name__ == '__main__':
    main()
