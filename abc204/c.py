import sys

def check(des, new):
    new = set(new)
    diff = des - new
    if new == diff:
        return None
    else:
        return des | new

def check_child(key, child, rd):
    target = set(child)
    diff = set(child)
    for i in diff:
        if i in rd:
            check_ele = set(rd[i])
            check_diff = target - check_ele
            if diff == check_ele:
                return 
            else:
                target = target | check_ele
                diff = check_diff

def main():
    s = sys.stdin.read().splitlines()

    n, m = map(int, s[0].split())
    roads = [(int(j) for j in i.split()) for i in s[1:n+1]]

    r_dict = {}

    for s,e in roads:
        if s not in r_dict:
            r_dict[s] = [e]
        elif e not in r_dict[s]:
            r_dict[s] += [e]
    
    


        

if __name__ == '__main__':
    main()
