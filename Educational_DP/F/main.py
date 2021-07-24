#!/usr/bin/env python3
import sys

def sinput():
    return sys.stdin.readline().rstrip('\n')

def dp(s,t):
    ls, lt = len(s), len(t)
    dp = [[0 for _ in range(lt+1)] for _ in range(ls+1)]

    for i in range(ls):
        for j in range(lt):
            if s[i] == t[j]:
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+1)
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    
    ans = ''
    i, j = ls, lt
    
    while i > 0 and j > 0:
        if dp[i][j] == dp[i-1][j]:
            i-=1
        elif dp[i][j] == dp[i][j-1]:
            j-=1
        else:
            i-=1
            j-=1
            ans += s[i]
    
    return ans[::-1]



def main():
    s = sinput()
    t = sinput()

    ans = dp(s,t)
    print(ans)

if __name__ == '__main__':
    main()
