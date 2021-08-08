import sys

def main():
    ans = 0

    # ここに回答
    a,b = map(int, input().split())

    while True:
        if a ^ ans == b:
            break
        ans += 1

    print(ans)

if __name__ == '__main__':
    main()