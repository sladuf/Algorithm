# 22.02.12 [두 용액]

import sys

n = int(sys.stdin.readline())
koi = list(map(int, sys.stdin.readline().split()))
koi.sort()

res = [0,0]
val = 2000000000
l = 0
r = n-1

while l < r:
    temp = koi[l]+koi[r]
    if abs(temp) < val:
        val = abs(temp)
        res = [koi[l],koi[r]]
    
    if temp < 0:
        l +=1
    elif temp > 0:
        r -=1
    else:
        break

print(res[0],res[1])