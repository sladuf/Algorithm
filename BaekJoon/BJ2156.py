# 22.02.17 [포도주 시식]
'''
f(0) = 0
f(1) = i
f(2) = i+(i-1)

f(i) = max(i+i-1+f(i-3) , i+f(i-2) , f(i-1))
'''
import sys

n = int(sys.stdin.readline())
juice = [0]
res = [0] * (n+1)
for i in range(n):
    juice.append(int(sys.stdin.readline()))

res[1] = juice[1]
if n>=2:
    res[2] = juice[2]+juice[1]

for i in range(3,n+1):
    temp1 = juice[i]+juice[i-1]+res[i-3]
    temp2 = juice[i]+res[i-2]
    temp3 = res[i-1]
    maxi = max([temp1, temp2, temp3])
    res[i] = maxi

print(res[n])