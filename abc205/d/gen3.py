import random

ele  = sorted(set([random.randint(1,10000) for i in range(100)]))
ele = [f'{i}' for i in ele]

que = set([random.randint(1,100) for i in range(5)])

print(len(ele), 4)

print(' '.join(ele))
for i in que:
    print(i)