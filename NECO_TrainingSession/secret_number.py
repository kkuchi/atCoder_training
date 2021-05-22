
import sys

def check(olist, xlist):
    ans = 0
    for i in range(10000):
        this_num = str(i).zfill(4)
        flag = False
        for o_ele in olist:
            if o_ele not in this_num:
                flag = True
                break
        for x_ele in xlist:
            if x_ele in this_num:
                flag = True
                break
        if flag: continue
        ans += 1
    return ans

def main():
    input_str = sys.stdin.readline()

    o_list = []
    x_list = []
    for num,flag in enumerate(input_str):
        str_num = str(num)
        if flag == 'o':
            o_list += [str_num]
        elif flag == 'x':
            x_list += [str_num]
    
    
    ans = check(o_list, x_list)
    print(ans)

main()
