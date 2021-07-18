a,b = map(int, input().split())

sum_min = a
sum_max = 6*a

if sum_min <= b and b <= sum_max:
    print('Yes')
else:
    print('No')