
import sys

def main():
    n, card_str = sys.stdin.readlines()[:2]
    card_list = sorted([int(i) for i in card_str.split()], reverse=True)

    a_list = card_list[0::2]
    b_list = card_list[1::2]

    print(sum(a_list) - sum(b_list))

main()
