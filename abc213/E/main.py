import sys
sinput = sys.stdin.readline

def main():
    h, w = map(int, sinput().split())
    pos = []
    for _ in range(h):
        pos += [sinput()]
    
    print(pos)

if __name__ == '__main__':
    main()