
pw = [int(i) for i in list(input())]

ans = 'Weak'

if pw == [pw[0]]*len(pw):
    print(ans)
else:
    for i in range(3):
        nxt = 0 if pw[i] == 9 else pw[i] + 1
        if pw[i+1] != nxt:
            ans = 'Strong'

    print(ans)