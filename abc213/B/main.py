import sys

def main():
    # ここに回答
    n = int(input())
    
    alist = [int(i) for i in input().split()]
    A = {}
    for i in range(1, n+1):
        A[i] = alist[i-1]
    
    res = sorted(A.items(), key=lambda x: x[1], reverse=True)
    print(res[1][0])

if __name__ == '__main__':
    main()