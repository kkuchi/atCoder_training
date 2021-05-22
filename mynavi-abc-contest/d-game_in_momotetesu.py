import sys

def main():
    INF = 1e10

    s = sys.stdin.read().splitlines()
    h, w = map(int, s[0].split())
    field = [list(i) for i in s[1:h+1]]

    # 座標とプラスマイナス
    MAP = [[1 if j == '+' else -1 for j in i] for i in field]

    # 座標と得点
    dp = [[0]*w]*h

    for i in reversed(range(h)):
        for j in reversed(range(w)):
            # 0,0 は飛ばす
            if i == h-1 and j == w-1:
                continue
            
            turn_num = 1 if (i+j)%2 == 0 else -1
            
            if i < h-2:
                r_pos = MAP[i+1][j]
                p_row = dp[i+1][j] + r_pos * turn_num
            else:
                p_row = INF * turn_num * -1

            if j < w-2:
                c_pos = MAP[i][j+1]
                p_col = dp[i][j+1] + c_pos * turn_num
            else:
                p_col = INF * turn_num * -1
            
            dp[i][j] = max(p_row, p_col) if turn_num == 1 else min(p_row, p_col)
    
    ans = dp[h-1][w-1]

    if ans == 0:
        print('Draw')
    elif ans > 0:
        print('Takahashi')
    else:
        print('Aoki')

main()