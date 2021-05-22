import sys
import math

def main():
    consumption_tax, num = [int(i) for i in sys.stdin.readline().split(' ')]

    # x = 100で計算, base_diff算出
    calclated_100_list = [calc(i, consumption_tax) for i in range(1, 100+1)]
    order_100 = set(range(1, calclated_100_list[-1]+1))
    calclated_100_set = set(calclated_100_list)
    
    base_diff = sorted(list(order_100 - calclated_100_set))

    # 周回の数と位置を確認
    loop = math.floor(num / consumption_tax)
    pos = num % consumption_tax

    # posが0の時は一つ前のループ
    if pos == 0:
        print(base_diff[-1]+(loop-1)*(100+consumption_tax))
    else:
        print(base_diff[pos-1]+loop*(100+consumption_tax))


def calc(x, tax):
    return (100+tax)*x // 100

main()