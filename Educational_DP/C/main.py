import sys

sinput = sys.stdin.readline
lsinput = lambda x: list(map(int, x.split()))

def calc(n, a):
    # 配列を作成
    dp = [[] for i in range(n)]
    # 最初の行はaと同じ
    dp[0] = a[0]
    # 1から繰り返し
    for i in range(1, n):
        # 3要素
        for j in range(3):
            # j以外のインデックスの最大値
            previous = max(dp[i-1][:j]+dp[i-1][j+1:])
            # a[i][j]足して決定
            dp[i] += [previous+a[i][j]]
    
    # 最終行の最大要素を返す
    return max(dp[-1])

def main():
    n = int(sinput())
    a = [lsinput(sinput()) for i in range(n)]

    ans = calc(n, a)

    print(ans)

if __name__ == '__main__':
    main()