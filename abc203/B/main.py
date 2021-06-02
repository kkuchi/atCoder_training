#!/usr/bin/env python3
import sys
import itertools

def main():
    n, k = map(int, input().split())

    ele = []

    for i,j in itertools.product(range(1,n+1), range(1,k+1)):
        ele += [int(f'{i}0{j}')]

    print(sum(ele))

if __name__ == '__main__':
    main()
