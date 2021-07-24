import sys

def read():
    return sys.stdin.readline().rstrip('\n')

def source():
    n = int(read())
    p = list(map(float, read().split()))

    return n, p


def calc(n, p):
    # 初期値は0
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

    # 左上を1にしておかないとすべて0になる
    dp[0][0] = 1

    # n枚投げる
    for i in range(n):
        # 表がj枚。上限はi
        for j in range(i+1):
            # 表の確率はi+1, j+1へ
            dp[i+1][j+1] += dp[i][j] * p[i]
            # 裏の確率はi+j, jへ
            dp[i+1][j] += dp[i][j] * (1 - p[i])
    
    req = n // 2 + 1
    res = sum(dp[n][req:])
    return res



def main():
    n, p = source()

    ans = calc(n, p)
    print(ans)

if __name__ == '__main__':
    main()
