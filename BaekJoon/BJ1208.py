# 21.03.08 [부분수열의 합2]
'''
개객개개개개 어려워...
counter + two-pointer + combination
1182번 부분수열의 합 업그레이드 문제임

1182번은 단순히 combinations으로 풀었지만
1208번은 범위가*2배 시간은 1/2배 되었기 때문에 다른 방법으로 접근해야함

문제 설명 : https://990427.tistory.com/48
'''
import sys
from itertools import combinations
from collections import defaultdict

n,s=map(int,sys.stdin.readline().split())
m=list(map(int, sys.stdin.readline().split()))


l=m[:n//2]
r=m[n//2:]

lsum=defaultdict(int)
rsum=defaultdict(int)
lsum[0]=1
rsum[0]=1
for i in range(1,len(l)+1):
    for com in combinations(l,i):
        lsum[sum(com)]+=1

for i in range(1,len(r)+1):
    for com in combinations(r,i):
        rsum[sum(com)]+=1

lkey=sorted(lsum.keys())
rkey=sorted(rsum.keys())

res=0
l=0
r=len(rkey)-1
while l<len(lkey) and r>=0:
    if lkey[l]+rkey[r]==s:
        res+=(lsum[lkey[l]]*rsum[rkey[r]])
        l+=1
        r-=1
    elif lkey[l]+rkey[r]>s:
        r-=1
    else:
        l+=1

if s==0:
    res-=1
    
print(res)
