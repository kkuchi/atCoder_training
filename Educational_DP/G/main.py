import sys
# 再帰の上限を上げておかないとREになる
sys.setrecursionlimit(100000)

g = []
dp = []

def source():
    global g

    # 読み込みのための関数
    spi = lambda x: map(int, x.split())
    # stdin一括読み
    s = sys.stdin.read().splitlines()

    # map(int)で読み
    n, m = spi(s[0])
    paths = [list(spi(row)) for row in s[1:]]

    # pathsからg(global変数)を作成
    g = [[] for _ in range(n+10)]
    for s,e in paths:
        g[s-1] += [e-1]

    return n, m


# 頂点からの最長パスを算出
def calc(child):
    # dpの値が-1　→　まだ計算していない
    if (dp[child] == -1):
        # 計算開始のため初期値を0に
        dp[child] = 0
        # 子要素を全て確認
        for i in g[child]:
            # 既存のdpの値と、子要素の頂点からの最長パス+1を比較
            dp[child] = max(dp[child], calc(i)+1)
    return dp[child]


# dp作成、各頂点の最長パスを作成して比較
def solve(n):
    global dp
    # dp初期値設定
    dp = [-1 for _ in range(n+10)]

    # 各頂点からの最長パス
    max_paths = [calc(i) for i in range(n)]
    # 一番長いものをreturn
    return max(max_paths)


# 実行
def main():
    n, m = source() # stdin読み
    ans = solve(n) # 算出
    print(ans)


if __name__ == '__main__':
    main()
