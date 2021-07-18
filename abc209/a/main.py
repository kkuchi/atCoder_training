a,b = map(int, input().split())

ans = 0 if a > b else b-a+1
print(ans)