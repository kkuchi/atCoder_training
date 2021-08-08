import sys
from collections import deque

def input_read():
    n = int(input())
    s = sys.stdin.read().splitlines()

    res = [[int(i) for i in row.split()] for row in s]
    
    G = [[] for _ in range(n)]
    for s, e in res:
        G[s-1] += [e-1]
        G[e-1] += [s-1]
    for i in range(n):
        G[i] = deque(sorted(G[i]))

    return n, G

def calc(n, G):
    check = [False for _ in range(n)]

    res = []

    q = deque([0])

    parent = {0: -1}

    while q:
        target = q.popleft()
        check[target] = True
        res += [target]
        for child in G[target]:
            # 未探索なら
            if not check[child]:
                q.append(child)
                parent[child] = target
                break
        
        if not q:
            if target == 0:
                break
            else:
                q.append(parent[target])
        
    return res


def main():
    n, G = input_read()
    res = calc(n, G)
    print(' '.join([str(i+1) for i in res]))

if __name__ == '__main__':
    main()