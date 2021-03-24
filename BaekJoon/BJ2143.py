# 21.03.09 [두 배열의 합]
import sys
from collections import defaultdict

n=int(sys.stdin.readline())

a=int(sys.stdin.readline())
A=list(map(int, sys.stdin.readline().split()))

b=int(sys.stdin.readline())
B=list(map(int, sys.stdin.readline().split()))

dic=defaultdict(int)
for i in range(a):
    temp=A[i]
    dic[temp]+=1
    for j in range(i+1,a):
        temp+=A[j]
        dic[temp]+=1

res=0
for i in range(b):
    temp=B[i]
    res+=dic[n-temp]
    for j in range(i+1,b):
        temp+=B[j]
        res+=dic[n-temp]

print(res)
