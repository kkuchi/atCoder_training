import sys

def main():
    s = sys.stdin.read().splitlines()
    n, k = map(int, s[0].split())
    c_list = s[1].split()

    ans = 0

    st_range = set(range(n-k+1))

    for i in st_range:
        target = len(set(c_list[i:i+k]))
        if target > ans:
            ans = target

    print(ans)
    
main()