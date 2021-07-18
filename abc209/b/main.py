
def main():
    n, x = map(int, input().split())
    a_list = [int(i) for i in input().split()]

    discount = n // 2

    total = sum(a_list) - discount

    if total <= x:
        print('Yes')
    else:
        print('No')

main()