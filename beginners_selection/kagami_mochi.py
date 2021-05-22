import sys
def main():
    s = sys.stdin.readlines()
    n = int(s[0])
    d = s[1:n+1]

    print(len(set(d)))

main()