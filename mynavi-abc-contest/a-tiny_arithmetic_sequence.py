
def main():
    in_list = [int(i) for i in input().split()]

    sorted_list = sorted(in_list)

    diffs = set([j - i for i,j in zip(sorted_list[:-1], sorted_list[1:])])

    if len(diffs) == 1:
        print('Yes')
    else:
        print('No')

main()