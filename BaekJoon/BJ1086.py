# 21.03.07 [부분합]
'''
2003 [수들의 합2] 의 연장선 문제
'''
import sys

n,s=map(int,sys.stdin.readline().split())
m=list(map(int, sys.stdin.readline().split()))+[0]

res=10001
l=0
r=0
total=m[0]
while r<n:
    if total>=s:
        res=min(res,r-l+1)
        total-=m[l]
        l+=1
        if l>r:
            r=l
            total=m[l]
    else:
        r+=1
        total+=m[r]

#최대길이로 저장해도 n이기 때문에 n보다 클 수 없다.
if res>n:
    print(0)
else:
    print(res)