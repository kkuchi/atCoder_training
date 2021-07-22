import sys

sinput = sys.stdin.readline

dp = []

def calc(list):
    for i in range(1, len(list)):
        if i == 1:
            dp[i] = abs(list[i] - list[i-1])
        else:
            one = dp[i-1] + abs(list[i] - list[i-1])
            two = dp[i-2] + abs(list[i] - list[i-2])

            dp[i] = min(one, two)

def main():
    global dp
    n = int(sinput())
    h_list = list(map(int, sinput().split()))

    dp = [0]*n

    calc(h_list)

    print(dp[-1])

if __name__ == '__main__':
    main()