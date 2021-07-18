# ネットで調べた解法
# 貪欲法

from math import factorial

def main():
    P = int(input())

    # 10から1までの階乗
    money = [factorial(i) for i in range(10, 0, -1)]
    # 答え
    ans = 0

    # 硬貨の種類で繰り返し
    for m in money:
        # Pがm以上ならmの効果を使う
        while m <= P:
            P -= m
            ans += 1

    print(ans)

main()