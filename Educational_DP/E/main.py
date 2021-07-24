import sys

def source():
    spi = lambda x: map(int, x.split())

    s = sys.stdin.read().splitlines()
    n, w = spi(s[0])
    goods = [list(spi(i)) for i in s[1:]]
    return n, w, goods


# dp計算
def calc(n, w, goods):
    # <dp[要素数][価値] = 重さの最小値> を作成する
    INF = 10 ** 9 + 1

    weights = [i[0] for i in goods]
    values = [i[1] for i in goods]

    value_max = sum(values)+1

    # dp作成、初期値はINF
    dp = [[INF for _ in range(value_max)] for _ in range(n+1)]

    # 最初だけ0に
    dp[0][0] = 0

    # dp更新
    for i in range(n):
        for j in range(value_max):
            dp1 = dp[i][j-values[i]] + weights[i] if j >= values[i] else INF
            dp2 = dp[i][j]
            dp3 = dp[i+1][j]

            dp[i+1][j] = min(dp1, dp2, dp3)

    # 最終行からINF以外取り出し
    last = {val:wei for val, wei in enumerate(dp[n]) if wei <= w}

    # ans取り出し
    return max(last.keys())
    
    
def main():
    # stdin
    n, w, goods = source()
    # dp計算
    ans = calc(n, w, goods)
    # 結果出力
    print(ans)


if __name__ == '__main__':
    main()