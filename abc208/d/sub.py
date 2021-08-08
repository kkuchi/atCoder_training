import sys, itertools, time

nrange = 0
dp = []

def source():
    global nrange, dp
    INF = 1 << 45
    spi = lambda x: map(int, x.split())
    s = sys.stdin.buffer.read().splitlines()

    n, m = spi(s[0])
    nrange = range(n)

    dp = [[[INF]*n for _ in nrange] for _ in nrange]

    for i in nrange:
        dp[i][i] = [0]*n

    for row in s[1:m+1]:
        a,b,c = spi(row)
        a -= 1
        b -= 1
        dp[a][b] = [c]*n
    
    return n, m

def calc(i, j, k):
    global dp
    if i == j:
        pass
    else:
        lim = 0 if k == 0 else k-1
        dp1 = dp[i][j][lim]
        dp2 = dp[i][k][lim] + dp[k][j][lim]
        dp[i][j][k] = min(dp1, dp2)
    

def solve():
    ans = 0
    for k in nrange:
        for i,j in itertools.product(nrange, nrange):        
            calc(i, j, k)
            res = dp[i][j][k]
            if res < 1 << 44:
                ans += res
    
    return ans

def main():
    n, m = source()
    ans = solve()
    print(ans)

if __name__ == '__main__':
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f'time: {end - start}')