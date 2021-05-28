import itertools, sys

def main():
    s = sys.stdin.read().splitlines()
    n,l = map(int, s[0])
    k = int(s[1])
    a_list = [int(i) for i in s[2]]

    res = []

    for ele in itertools.combinations(range(n), k):
        top_ele = a_list[ele[0]]
        if k == 1:
            min_ele = min(top_ele, l - top_ele)
        else:
            len_ele = [top_ele] + [
                a_list[ele[i+1]] - a_list[ele[i]]
                for i in range(k-1)
            ]
            len_ele += [l - a_list[ele[-1]]]

            min_ele = min(len_ele)

        res += [min_ele]

    print(max(res))

main()