
import sys

def main():
    n, a_str = sys.stdin.readlines()[:2]

    n = int(n)
    a_list = [int(i) for i in a_str.strip('\n').split(' ')]

    ans = []

    for i in range(61):
        count_one = 0
        for ele in a_list:
            if (ele >> i) & 1:
                count_one += 1
        count_zero = n - count_one

        ans += [count_one * count_zero * (2 ** i)]

    print(sum(ans) % (10 ** 9 + 7))

main()