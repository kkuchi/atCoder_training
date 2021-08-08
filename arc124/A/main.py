import sys

sinput = sys.stdin.readline

def spi(mode):
    ele = sinput().split()
    # both
    if mode == "b":
        return map(int, ele)
    # right
    elif mode == "r":
        ele[-1] = int(ele[-1])
        return ele


def calc(n, k, r):
    
    pass


def main():
    n, k = spi('b')
    restriction = [spi('r') for _ in range(k)]
    ans = calc(n, k, restriction)

main()