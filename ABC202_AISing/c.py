# PyPyで提出

import sys
from collections import Counter

def sp_list(e):
    return list(map(int, e.split()))

def main():
    s = sys.stdin.read().splitlines()
    A, B, C = map(sp_list, s[1:4])

    target = [B[c-1] for c in C]

    counter = Counter(target)
    c_keys = counter.keys()

    ans = [counter[a] for a in A if a in c_keys]

    print(sum(ans))

main()