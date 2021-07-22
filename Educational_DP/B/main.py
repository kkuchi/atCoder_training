import sys

sinput = sys.stdin.readline

dp = []

def calc(list, n ,k):
    for i in range(1, n):
        if i < k:
            compare = [dp[j] + abs(list[i] - list[j]) for j in range(i)]
            dp[i] = min(compare)
        else:
            compare = [dp[i-j] + abs(list[i] - list[i-j]) for j in range(k, 0, -1)]
            dp[i] = min(compare)


def main():
    global dp
    n, k = map(int, sinput().split())
    h_list = list(map(int, sinput().split()))

    dp = [0]*n
    calc(h_list, n, k)

    print(dp[-1])

if __name__ == '__main__':
    main()
