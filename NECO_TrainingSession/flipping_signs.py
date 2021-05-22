import sys

def main():
    n, a_list = sys.stdin.readlines()[:2]
    # 数値化・リスト化
    n = int(n)
    a_list = [int(i) for i in a_list.strip('\n').split(' ')]

    # a_listを絶対値に。sortしておく
    abs_a = sorted([abs(i) for i in a_list])

    # 負の数が偶数なら全て正の数に出来る
    count_minus = len([i for i in a_list if i < 0])
    # 0があれば-を押し付けて無視できる
    include_zero = True if 0 in a_list else False

    if count_minus % 2 != 0 and not include_zero:
        abs_a[0] *= -1
    
    print(sum(abs_a))

main()