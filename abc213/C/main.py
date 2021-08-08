import sys, bisect

def main():
    rl = sys.stdin.buffer.readline
    read = sys.stdin.buffer.read
    spi = lambda x: map(int, x.split())
    # ここに回答

    h, w, n = spi(rl())

    pos = [[int(i) for i in row.split()] for row in read().splitlines()]

    card_row = set()
    card_col = set()

    for r, c in pos:
        card_row.add(r)
        card_col.add(c)
    
    card_row = list(card_row)
    card_row.sort()
    card_col = list(card_col)
    card_col.sort()
    
    for r, c in pos:
        row = bisect.bisect_left(card_row, r)
        col = bisect.bisect_left(card_col, c)
        print(row+1, col+1)

if __name__ == '__main__':
    main()