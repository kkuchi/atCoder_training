import sys
from numba import jit

# pとインデックスをもらい、parentを返す
def node(p: list, num: int, tree=None):
    parent = p[num-2]
    return tree[parent] + [num]

# @jit
def tree_gen(p: list, n: int):
    tree = {1: [1]}
    for i in range(2,n+1):
        tree[i] = node(p, i, tree)
    return tree

@jit
def check(query: list, tree: dict):
    for u,d in query:
        match_ele = [i for i in tree.values() if u in i and len(i)-1 == d]
        print(len(match_ele))

def main():
    s = sys.stdin.read().splitlines()

    n = int(s[0])
    p = [int(i) for i in s[1].split()]

    q = int(s[2])
    query = [[int(j) for j in i.split()] for i in s[3:3+q]]

    tree = tree_gen(p, n)

    check(query, tree)

main()