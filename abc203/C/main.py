#!/usr/bin/env python3
import sys

def main():
    s = sys.stdin.read().splitlines()

    n, k = map(int, s[0].split())
    friends = [[int(j) for j in i.split()] for i in s[1:n+1]]
    bonus = {}
    for friend in friends:
        if friend[0] not in bonus:
            bonus[friend[0]] = friend[1]
        else:
            bonus[friend[0]] += friend[1]

    current_pos = 0

    for pos, money in sorted(bonus.items()):
        diff = pos - current_pos
        if k - diff < 0:
            print(current_pos + k)
            return 0
        else:
            k -= diff
            current_pos = pos
            k += money
    
    print(current_pos + k)

if __name__ == '__main__':
    main()
