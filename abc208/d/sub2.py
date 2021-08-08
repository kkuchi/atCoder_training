import sys, itertools

def main():
    spi = lambda x: map(int, x.split())
    s = sys.stdin.buffer.read().splitlines()

    n,m = spi(s[0])
    abc = [list(spi(row)) for row in s[1:]]

    dp = [[1 << 60]*n for _ in range(n)]
    for a, b, c in abc:
        dp[a-1][b-1] = c
    
    ans = 0

    for k in range(n):
        nxt = [[0]*n for _ in range(n)]
        for i,j in itertools.product(range(n), range(n)):
            if i == j:
                continue
            nxt[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
            if nxt[i][j] < 1 << 59:
                ans += nxt[i][j]
        dp = nxt
    
    print(ans)

if __name__ == '__main__':
    main()