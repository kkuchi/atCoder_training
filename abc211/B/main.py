import sys

s = sys.stdin.read().splitlines()

ans = 'Yes'

if 'H' in s:
    pass
else:
    ans = 'No'

if '2B' in s:
    pass
else:
    ans = 'No'

if '3B' in s:
    pass
else:
    ans = 'No'

if 'HR' in s:
    pass
else:
    ans = 'No'

print(ans)