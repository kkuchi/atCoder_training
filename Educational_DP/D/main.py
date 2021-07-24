import sys

def source():
    s = sys.stdin.read().splitlines()
    n, w = map(int, s[0].split())
    goods = [list(map(int, i.split())) for i in s[1:]]
    return n, w, goods


def calc(n, w, goods):
    dp = [[0 for i in range(w+1)] for j in range(n+1)]

    for i in range(n):
        for j in range(w+1):
            dp1 = 0
            if j >= goods[i][0]:
                dp1 = dp[i][j-goods[i][0]] + goods[i][1]
            dp2 = dp[i][j]
            dp[i+1][j] = max(dp1, dp2)

    return dp


def main():
    n, w, goods = source()
    dp = calc(n, w, goods)
    print(dp[n][w])


if __name__ == '__main__':
    main()