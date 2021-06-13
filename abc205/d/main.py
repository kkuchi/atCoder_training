import sys

def main():
    s = sys.stdin.read().splitlines()

    n, q = map(int, s[0].split())
    a_set = set([int(i) for i in s[1].split()])
    k_list = [int(i) for i in s[2:n+1]]

    target = set(range(1, max(k_list)+len(a_set)+1)) - a_set
    target = sorted(target)

    out_ele = [str(target[i-1]) for i in k_list]
    print('\n'.join(out_ele))

main()

