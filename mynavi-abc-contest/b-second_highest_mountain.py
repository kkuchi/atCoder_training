import sys

def main():
    s = sys.stdin.read().splitlines()

    n = int(s[0])
    mountains = [i.split() for i in s[1:n+1]]
    mountains = [[i[0], int(i[1])] for i in mountains]

    mountains.sort(key=lambda x: x[1], reverse=True)

    print(mountains[1][0])

main()