import sys, bisect

def _main():
    s = sys.stdin.read().splitlines()

    n, q = map(int, s[0].split())
    a_set = set([int(i) for i in s[1].split()])
    k_list = [int(i) for i in s[2:n+1]]

    target = set(range(1, max(k_list)+len(a_set)+1)) - a_set
    target = sorted(target)

    out_ele = [str(target[i-1]) for i in k_list]
    print('\n'.join(out_ele))


def main():
    s = sys.stdin.read().splitlines()

    n, q = map(int, s[0].split())
    a_list = [int(i) for i in s[1].split()]
    k_list = [int(i) for i in s[2:n+1]]

    b = [0]+[v - i - 1 for i,v in enumerate(a_list)]

    for k in k_list:
        key = bisect.bisect_right(b, k-1)
        print(key)
        print(a_list[key-1] + (k - b[key-1]))

main()

