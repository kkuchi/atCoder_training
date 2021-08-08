# おまじない
import sys
sys.setrecursionlimit(300000)

# 読み
N=int(input())
# グラフ
G=[[] for i in range(N+1)]
for i in range(N-1):
    a,b=map(int,input().split())
    G[a].append(b)
    G[b].append(a)

# ソート
for i in range(N+1):G[i].sort()

# 答え
ans=[]
# current, previous
def dfs(crr,pre):
    print('cr, pre:', crr, pre)
    # currentをansへ
    ans.append(crr)
    # グラフから次を確認
    for nxt in G[crr]:
        # sort済なので、preではない最初の要素が最小
        # なければ終了
        if nxt!=pre:
            # dfs
            dfs(nxt,crr)
            # 戻ってきた時
            ans.append(crr)

dfs(1,-1)
print(*ans)