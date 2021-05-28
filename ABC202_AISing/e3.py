import sys

def check(p):
    p = [None] + p
    ele = {i+1:v for i,v in enumerate(p)}

    res = {}

    for i,v in ele.items():
        dist = 0
        if v == None:
            res[i] = 0
            continue
        elif v == 1:
            res[i] = 1
        else:
            item = v
            while True:                
                dist += 1
                if item == 1: break
                else: item = ele[item]
            res[i] = dist

    return res

def tree_gen2(n, p):
    tree = {i:[[j+2 for j, _x in enumerate(p) if _x == i]] for i in range(1, n+1) if i in p}
    tree = {i:[[i]]+v+sum([tree[j] for j in v[0] if j in tree], []) for i,v in tree.items()}

    dist = check(p)

    return tree, dist


def tree_gen(n, p):
    tree = {}
    for i in range(n):
        target = [index+2 for index, val in enumerate(p) if val == i+1]
        tree[i+1] = target
    tree = {i:v for i,v in tree.items() if v != []}
    print(tree)
    keys = tree.keys()
    for i in keys:
        tree[i+1] += [tree[j] for j in tree[i+1] if j in keys]
    print(tree)
    pass

def main():
    # 入力と取り出し
    stdi = sys.stdin.read().splitlines()
    n, p, q = stdi[:3]
    n, q = map(int, (n, q))
    p = [int(i) for i in p.split()]
    queries = [[int(j) for j in i.split()] for i in stdi[3:3+q]]

    tree, dist = tree_gen2(n, p)
    
    for u,d in queries:
        if u in tree:
            diff = d - dist[u]
            print(len(tree[u][diff]))
        else:
            if d == dist[u]:
                print(1)
            else:
                print(0)

main()