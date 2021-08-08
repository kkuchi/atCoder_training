import sys

def main():
    rl = sys.stdin.buffer.readline
    read = sys.stdin.buffer.read
    spi = lambda x: map(int, x.split())

    n, m, k = spi(rl())
    disable_roads = [list(spi(row)) for row in read().splitlines()]

    nlist = range(n)

    G = []
    for i in range(n):
        ele = [j for j in nlist if j != i]
        G += [ele]

    for u, v in disable_roads:
        G[v-1].remove(u-1)
        G[u-1].remove(v-1)

    dp = [1] + [0]*(n-1)

    for _ in range(k):
        ndp = [0]*n
        for j in range(n):
            check = [dp[ind] for ind in G[j]]
            ndp[j] = sum(check)
        dp = ndp
    
    MOD = 998244353
    print(dp[0] % MOD)


main()
