import sys

class Node():
    def __init__(self, p_node, this_num=None):
        if p_node == []:
            self.prev = [1]
            self.dist = 0
        else:
            pp = p_node.prev
            self.prev = pp + [this_num]
            self.dist = len(pp)


def tree_gen(n, p):
    tree = [ Node([]) ]
    for i in range(1, n):        
        tree += [Node(tree[p[i-1]-1], i+1)]
    return tree


def main():
    stdi = sys.stdin.read().splitlines()
    n = int(stdi[0])
    p = [int(i) for i in stdi[1].split()]
    q = int(stdi[2])
    queries = [[int(j) for j in i.split()] for i in stdi[3:3+q]]

    tree = tree_gen(n, p)

    for u, d in queries:
        ans = [node for node in tree if node.dist == d and u in node.prev]
        print(len(ans))
    
main()