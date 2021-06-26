from collections import deque

s = """\
3 3
1 2
2 3
3 2
"""

tree = [[int(i) for i in row.split()] for row in s.split('\n')]

queue = deque([0])
while queue:
    now = queue.popleft()
    print(now)
    for i in tree[now]:
        queue.append(i)


