import sys

def sinput():
    ele = sys.stdin.readline()
    return ele.rstrip('\n')

n, k = map(int, sinput().split())

alist = [int(i) for i in sinput().split()]
adict = {i:v for i,v in enumerate(alist)}
s_adict = dict(sorted(adict.items(), key=lambda x: x[1]))

num = k // n
kd = k % n

if kd == 0:
    for i in range(n):
        print(num)
else:
    scores = {i: num for i in s_adict.keys()}
    count = 0
    for i,v in scores.items():
        scores[i] += 1
        count += 1
        if count == kd:
            break

    for i,v in sorted(scores.items()):
        print(v)