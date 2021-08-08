import sys

goal = -1
g = []

def spi(x):
    return map(int, x.split())

def source():
    global g
    s = sys.stdin.read().splitlines()
    n, m = spi(s[0])
    roads = [list(spi(row)) for row in s[1:]]

    g = [[] for _ in range(n)]

    for s,e in roads:
        g[s-1] += [e-1]
        g[e-1] += [s-1]

    return n, m, roads

def calc(child):
    if child == goal:
        return 
    children = g[child]
    


def solve(n):
    global goal
    goal = n-1
    # 最小時間、経路数
    dp = [[] for _ in range(n)]




def main():
    MOD = 10 ** 9 + 7
    n, m, roads = source()

    dp = solvep(n)


if __name__ == '__main__':
    main()