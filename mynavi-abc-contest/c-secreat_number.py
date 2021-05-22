def main():
    s = input()
    olist = []
    xlist = []

    for i, char in enumerate(s):
        i = str(i)
        if char == 'o':
            olist += [i]
        elif char == 'x':
            xlist += [i]
    
    if len(olist) > 4:
        print(0)
        return 0

    ans = []

    for ele in range(10000):
        ele = str(ele).zfill(4)
        flag = True

        for o_ele in olist:
            if o_ele not in ele:
                flag = False
                break
        
        if flag:
            for x_ele in xlist:
                if x_ele in ele:
                    flag = False
                    break
        if flag:
            ans += [ele]
    
    print(len(ans))

main()
