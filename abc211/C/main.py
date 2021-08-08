
def calc(s):
    check = 'chokudai'
    ls = len(s)
    dp = [[1] + [0 for _ in range(8)] for _ in range(ls+1)]    

    for i in range(1, ls+1):
        for j in range(1, 9):
            if s[i-1] == check[j-1]:
                ltop = dp[i-1][j-1]
                top = dp[i-1][j]
                dp[i][j] = ltop + top
            else:
                dp[i][j] = dp[i-1][j]

    return dp[ls][8]


def main():
    MOD = 10 ** 9 + 7

    s = input()
    ans = calc(s) % MOD
    print(ans)


if __name__ == '__main__':
    main()
