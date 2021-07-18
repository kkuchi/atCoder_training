import bisect

def main():
    # 1 <= p <= 10 ** 7
    p = int(input())

    count = 1
    current = 1
    nums = []

    while True:
        current *= count
        nums += [current]
        if p <= current:
            break
        else:
            count += 1

    count -= 1
    nums = nums[:-1]

    target = p
    maisuu = 0

    while True:
        index = bisect.bisect_left(nums, target)

        if index >= count:
            index = -1
        elif target < nums[index]:
            index -= 1
        
        maisuu += 1
        target -= nums[index]
        
        if target == 0:
            break

    print(maisuu)

if __name__ == '__main__':
    main()