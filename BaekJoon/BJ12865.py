# 22.02.18 [평범한 배낭]

import sys

n,k = map(int, sys.stdin.readline().split())
m = []
for i in range(n):
    w,v = map(int,sys.stdin.readline().split())
    m.append([w,v])

bag = [0] * (k+1)

for i in range(n):
    w,v = m[i]
    for j in range(k,0,-1):
        if w > j:
            break
        bag[j] = max([bag[j], bag[j-w]+v])

print(bag[-1])