def main():
    n, k = map(int, input().split())
    c_list = input().split()

    tmp = {i: 0 for i in c_list}

    ans = 0

    for i in range(k):
        tmp[c_list[i]] += 1
    
    for i in range(n-k):
        target = len([v for v in tmp.values() if v != 0])
        ans = max(ans, target)
        tmp[c_list[i]] -= 1
        tmp[c_list[i+k]] += 1
    
    print(ans)

main()