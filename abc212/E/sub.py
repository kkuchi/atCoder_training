import sys

def main():
    rl = sys.stdin.buffer.readline
    read = sys.stdin.buffer.read
    spi = lambda x: map(int, x.split())

    n, m, k = spi(rl())
    disable_roads = [list(spi(row)) for row in read().splitlines()]

    G = [[] for _ in range(n)]
    for s,t in disable_roads:
        s -= 1
        t -= 1
        G[s] += [t]
        G[t] += [s]
    
    dp = [1] + [0]*(n-1)

    for _ in range(k):
        nxt = [0]*n
        all_res = sum(dp)
        for i in range(n):
            check = 0
            for item in G[i]:
                check += dp[item]
            nxt[i] = all_res - dp[i] - check
        dp = nxt
    
    MOD = 998244353
    
    print(dp[0] % MOD)

main()