# 22.03.18 [기타줄]

import sys

n,m = map(int, sys.stdin.readline().split())
six = []
one = []
for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    six.append(a)
    one.append(b)

six.sort()
one.sort()

res = 0

temp = n//6
small = six[0] if six[0] < one[0]*6 else one[0]*6
res += small*temp

temp = n%6
small = six[0] if six[0] < one[0]*temp else one[0]*temp

res += small

print(res)