
def main():
    a,b,c = map(int, input().split())

    # cが偶数なら
    if c % 2 == 0:
        diff = abs(a) - abs(b)
    else:
        diff = a - b
    
    if diff == 0:
        print('=')
    elif diff > 0:
        print('>')
    else:
        print('<')

main()