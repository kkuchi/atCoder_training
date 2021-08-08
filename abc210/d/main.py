import sys

def source():
    spi = lambda x: map(int, x.split())
    s = sys.stdin.read().splitlines()

    h, w, c = spi(s[0])
    A = [list(spi(row)) for row in s[1:]]

    return h, w, c, A


def calc(h, w, c, A):
    pass


def main():
    h, w, c, A = source()
    # cost = A(s) + A(e) + c * ((ex - sx) + (ey - sy))
    # → = A(e) + c*(ey + ex) + A(s) - c*(sy + sx)


if __name__ == '__main__':
    main()