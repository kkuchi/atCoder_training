
def main():
    n,a,b = map(int, input().split())

    n_sums = [sum([int(j) for j in list(str(i))]) for i in range(1, n+1)]

    target_sums = [i+1 for i,v in enumerate(n_sums) if v >= a and v <= b]

    print(sum(target_sums))

main()