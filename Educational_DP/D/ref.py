n, w = map(int,input().strip().split())
wv = []
for i in range(n):
    array = list(map(int, input().strip().split()))
    wv.append(array)

dp = [[0 for j in range(100010)]for i in range(110)]  # ※1

for i in range(n):
    print('i', i)
    print('wv[i][0]', wv[i][0])
    print(dp[i][:w+1])
    for sum_w in range(w+1):
        print('sum_w', sum_w)
        print('dp[i+1][sum_w]', dp[i+1][sum_w])
        
        if sum_w - wv[i][0] >= 0: # ターゲットの値を足してsum_wになる要素がdpにある
            dp1 = dp[i][sum_w - wv[i][0]] + wv[i][1]
        # なければ前のloopと同じものを入れる
        dp2 = dp[i][sum_w]

        if sum_w - wv[i][0] >= 0 and dp1 > dp[i+1][sum_w]:
            dp[i+1][sum_w] = dp1
        if dp2 > dp[i+1][sum_w]:
            dp[i+1][sum_w] = dp2

print(dp[n][w])