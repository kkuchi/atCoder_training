import sys
from collections import deque

def main():
    s = sys.stdin.read().splitlines()
    n, k = map(int, s[0].split())
    C = s[1].split()

    color = {}
    ans = 0
    tmp = 0

    for i in range(n):
        color[C[i]] = 0
    
    for i in range(k):
        if color[C[i]] == 0:
            tmp += 1
        color[C[i]] += 1
    
    ans = tmp

    for i in range(n-k):
        if color[C[i]] == 1:
            tmp -= 1
        color[C[i]] -= 1
        
        if color[C[k+i]] == 0:
            tmp += 1
        color[C[k+i]] += 1

        ans = max(ans, tmp)

    print(ans)
    
if __name__ == '__main__':
    main()