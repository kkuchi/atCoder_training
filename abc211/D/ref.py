import sys
from collections import deque

def source():
    # 準備
    spi = lambda x: map(int, x.split())
    # stdin一括読み
    s = sys.stdin.read().splitlines()
    # 最初の行
    n, m = spi(s[0])
    # グラフ作成
    g = [[] for _ in range(n)]
    for row in s[1:]:
        a,b = spi(row)
        a -= 1
        b -= 1
        g[a] += [b]
        g[b] += [a]
    
    return n, g


def calc(n, g):
    MOD = 10 ** 9 + 7 # mod
    
    dp = [0]*n # 経過。この場合は深さ
    num = [1] + [0]*(n-1) # 結果
    q = deque([0]) # キュー
    visited = [True] + [False]*(n-1) # 確認したかどうか
    
    # キューの中身がなくなるまで繰り返し
    while q:
        # 先頭から取り出し
        from1 = q.popleft()
        # 子要素を一つずつ処理
        for to in g[from1]:
            # 未探索なら
            if not visited[to]:
                # 深さなのでfromに1足す
                dp[to] = dp[from1] + 1
                # パターンの数はfromから引き継ぐ
                num[to] = num[from1]
                # 探索済みに
                visited[to] = True
                # toをキューに
                q.append(to)
            # 探索済み、既に入っている深さと今回の深さが同じ場合
            elif dp[to] == dp[from1] + 1:
                # 最短経路の個数を追加
                num[to] += num[from1]
    # 剰余
    ans = num[-1] % MOD

    return ans


def main():
    n, g = source()
    ans = calc(n, g)
    print(ans)


if __name__ == '__main__':
    main()