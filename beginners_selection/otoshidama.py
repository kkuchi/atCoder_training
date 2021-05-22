import itertools

def calc(t, n):
    return 10000*t[0] + 5000*t[1] + 1000*(n - sum(t))

def main():
    n,y = map(int, input().split())
    l = [i for i in itertools.product(range(n+1), repeat=2) if sum(i) <= n]
    
    exist_l = [[i[0], i[1], n-sum(i)] for i in l if calc(i, n) == y]
    
    if len(exist_l) == 0:
        print('-1 -1 -1')
    else:
        ele = exist_l[0]
        print(f'{ele[0]} {ele[1]} {ele[2]}')

def sub():
    n,y = map(int, input().split())

    for i in range(n+1):
        for j in range(n+1):
            if i+j > n: continue
            if 10000*i+5000*j+1000*(n-i-j) == y:
                print(i,j,(n-i-j))
                return 0
    
    print('-1 -1 -1')


main()
# sub()
