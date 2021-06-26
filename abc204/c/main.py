import sys
from collections import deque

# read
S = sys.stdin.read().splitlines()
# 街の数、道の数
n, m = map(int, S[0].split())
# 道
roads = [[int(i)-1 for i in row.split()] for row in S[1:m+1]]
# 答え
ans = 0

# 幅優先探索
def bfs(i):
    global ans
    print(i)
    # 行った街は1に
    visited = [0]*n
    # deque
    que = deque()
    que.append(i)
    visited[i] = 1
    ans += 1

    while len(que) != 0:
        print('before:', que)
        tar = que.popleft()
        print('after:', que)
        for j in roads[tar]:
            if visited[j] == 0:
                que.append(j)
                visited[j] = 1
                ans += 1

for i in range(n):
    bfs(i)
print(ans)

