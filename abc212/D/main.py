import sys
from bisect import bisect_left

def main():
    read = sys.stdin.buffer.readline
    spi = lambda x: map(int, x.split())

    [q] = list(spi(read()))

    bag = []
    ans = []

    for _ in range(q):
        query = list(spi(read()))
        op_type = query[0]
        if op_type == 3:
            ans += [bag.pop(0)]
        else:
            op_val = query[1]
            if op_type == 1:
                index = bisect_left(bag, op_val)
                bag.insert(index, op_val)
            elif op_type == 2:
                bag = list(map(lambda x: x+op_val, bag))

    [print(i) for i in ans]

main()