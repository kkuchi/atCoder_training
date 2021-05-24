import itertools
from math import comb

def check(s, a, b, k):
    check_k = comb(a+b-1, a-1)    
    if k > check_k:
        s += 'b'
        b -= 1
        k -= check_k
    else:
        s += 'a'
        a -= 1

    return s, a,b, k

def sub():
    a,b,k = map(int, input().split())
    rem_a = a
    rem_b = b
    rem_k = k

    s = ''

    while rem_a > 0 and rem_b > 0:
        s, rem_a, rem_b, rem_k = check(s, rem_a, rem_b, rem_k)
    
    
    if rem_a == 0: s += 'b'*rem_b
    else: s += 'a'*rem_a
    
    print(s)
sub()