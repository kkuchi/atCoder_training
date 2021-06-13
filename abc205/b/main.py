def main():
    n = int(input())

    a_list = [int(i) for i in input().split()]

    if len(a_list) != n:
        print('No')

    ele = set(range(1, n+1))

    if ele == set(a_list):
        print('Yes')
    else:
        print('No')

main()