import sys
import itertools

def main():
    a,b,c,x = map(int, sys.stdin.readlines()[:4])

    prices = []

    for a_,b_,c_ in itertools.product(range(a+1), range(b+1), range(c+1)):
        prices += [500*a_ + 100*b_ + 50*c_]
    
    print(prices.count(x))

main()