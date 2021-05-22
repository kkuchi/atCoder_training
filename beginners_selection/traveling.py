import sys

def main():
    s = sys.stdin.read().splitlines()
    n = int(s[0])
    l = list(map(str.split, s[1:n+1]))
    l = [[int(j) for j in i] for i in l]

    # 最初のチェック
    f_obj = l[0]
    check_num = f_obj[0] - sum(f_obj[1:])
    if check_num < 0 or check_num % 2 == 1:
        print('No')
        return 0

    # 時間と最短時間の差が偶数か奇数かで判断
    for [t1, x1, y1], [t2, x2, y2] in zip(l[:-1], l[1:]):
        time = t2 - t1
        min_time = abs(x2 - x1) + abs(y2 - y1)

        check_time = time - min_time

        if check_time == 0:
            continue
        elif check_time < 0 or check_time % 2 == 1:
            print('No')
            return 0
    
    print('Yes')


main()