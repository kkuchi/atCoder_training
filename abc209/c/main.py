
def main():
    # 剰余
    MOD = 10 ** 9 + 7
    # 読み
    n = int(input())
    C = [int(i) for i in input().split()]    
    C.sort() # ソートする

    # dp初期設定
    dp = [0]*n
    dp[0] = C[0]

    # dp処理
    for i in range(1, n):
        # 前のdp * (ターゲットの数値 - これまでの要素数)
        tmp = dp[i-1] * (C[i] - i)
        dp[i] = tmp % MOD
    
    print(dp[-1])
    
main()