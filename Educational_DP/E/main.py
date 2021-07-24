import sys

def source():
    s = sys.stdin.read().splitlines()
    n, w = map(int, s[0].split())
    goods = [list(map(int, i.split())) for i in s[1:]]
    return n, w, goods

def calc(n, w, goods):
    INF = 10 ** 9 + 1
    cols = sum([i[1] for i in goods])
    # dp[i][v]は、i-1番目までの品物から価値vになるよう選んだ時の重さの最小値
    dp = [[0 for _ in range(cols)] for __ in range(n+1)]
    
    for i in range(n):
        for j in range(cols):
            print('j', j, 'goods[i][1]', goods[i][1])
            dp1 = 0
            if j >= goods[i][1]:
                dp1 = dp[i][j-goods[i][1]] + goods[i][0]
            dp2 = dp[i][j]
            
            if dp1 == dp2 == 0:
                pass
            else:
                dp1 = INF if dp1 == 0 else dp1
                dp2 = INF if dp2 == 0 else dp2
            dp[i+1][j] = min(dp1, dp2)
    
    # 価値:重さ
    res = {i:v for i,v in enumerate(dp[n]) if v <= w}
    print(res)

    return max(res.keys())


def main():
    n, w, goods = source()

    ans = calc(n, w, goods)

    print(ans)


if __name__ == '__main__':
    main()