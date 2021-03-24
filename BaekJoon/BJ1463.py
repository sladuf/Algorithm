# 21.01.28 [1로 만들기]

import sys

n = int(sys.stdin.readline())

result = [0 for i in range(n+1)]
for i in range(2, n+1):
    result[i] = result[i-1]+1
    if i%2==0 and result[i] > result[i//2]+1:
        result[i] = result[i//2]+1
    if i%3==0 and result[i] > result[i//3]+1:
        result[i] = result[i//3]+1
        
print(result[n])
