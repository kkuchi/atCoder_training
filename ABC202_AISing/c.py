import sys

def sp_list(e):
    return list(map(int, e.split()))

def main():
    s = sys.stdin.read().splitlines()
    # n = s[0]
    A, B, C = map(sp_list, s[1:4])

    target = [B[c-1] for c in C]

    t_count = [target.count(a) for a in A]

    print(sum(t_count))

main()