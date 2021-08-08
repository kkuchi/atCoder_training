import sys
from collections import deque

dp = []
G = []

def source():
    global dp, G
    spi = lambda x: map(int, x.split())
    s = sys.stdin.read().splitlines()
    
    n, m = spi(s[0])
    G = [{} for _ in range(n)]
    for row in s[1:m+1]:
        a,b,c = spi(row)
        a -= 1
        b -= 1
        G[a][b] = c
    
    dp = [[[-1 for _ in range(n)] for _ in range(n)] for _ in range(n)]
    
    return n, m, G

def bfs(s, t, k):
    global dp
    if s == t:
        dp[s][t][k] = 0
        return 0

    q = deque([s])
    while q:
        target = q.popleft()
        children = G[target]
        if t in children.keys():
            dp[s][t][k] = dp[s][target][k] + children[t]
            break
        for child, cost in children.items():
            if child <= k:
                if dp[s][child][k] == -1:
                    dp[s][child][k] = dp[s][target][k] + cost
                else:
                    dp[s][child][k] = min(dp[s][target][k] + cost, dp[s][child][k])
                q.append(child)
                # else:
                #     dp[s][child][k] = min(dp[s][target][k] + 1, p[s][child][k])
    if dp[s][t][k] == -1:
        dp[s][t][k] = 0

def calc(n, m, G):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                bfs(i, j, k)
    
    tmp = [[sum(d2) for d2 in d1] for d1 in dp]
    tmp2 = [sum(d1) for d1 in tmp]

    ans = sum(tmp2)

    return ans


def main():
    n, m, G = source()
    ans = calc(n, m, G)
    print(dp)
    print(ans)

if __name__ == '__main__':
    main()