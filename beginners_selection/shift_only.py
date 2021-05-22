def main():
    n = int(input())
    a_list = [int(i) for i in input().split()]

    count = 0
    while True:
        for ele in a_list:
            if ele % 2 == 1:
                print(count)
                return 0
        a_list = [i/2 for i in a_list]
        count += 1
    

main()