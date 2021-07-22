import bisect
from math import factorial

def main():
    # 1 <= p <= 10 ** 7
    p = int(input())

    coins = [factorial(i) for i in range(1,11)]

    count = 0

    while True:
        check = bisect.bisect_right(coins, p)

        if check == 0:
            count += p
            break
        
        p -= coins[check-1]
        count += 1

        if p == 0:
            break
    
    print(count)

if __name__ == '__main__':
    main()