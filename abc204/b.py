
n = int(input())

A = [int(i) for i in input().split()]

res = [0 if i <= 10 else i - 10 for i in A]

print(sum(res))