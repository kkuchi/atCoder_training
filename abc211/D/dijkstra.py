import sys

def spi(x):
    return map(int, x.split())

def source():
    s = sys.stdin.read().splitlines()
    n, m = spi(s[0])
    roads = [list(spi(row)) for row in s[1:]]

    adj = [[] for _ in range(n)]

    for s,e in roads:
        adj[s-1] += [(e-1, 1)]
        adj[e-1] += [(s-1, 1)]

    return n, m, adj

from heapq import heappush, heappop
INF = 10 ** 9
def dijkstra(s, n, adj):
    dist = [INF] * n
    hq = [(0, s)]
    dist[s] = 0
    seen = [False] * n
    while hq:
        v = heappop(hq)[1]
        seen[v] = True
        for to, cost in adj[v]:
            if seen[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
    return dist

def main():
    n, m, adj = source()
    ans = dijkstra(0, n, adj)
    print(ans)


if __name__ == '__main__':
    main()