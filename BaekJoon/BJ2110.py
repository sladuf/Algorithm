# 21.02.19 [공유기 설치]
import sys

n,c = map(int, sys.stdin.readline().split())

x = []
for i in range(n):
    x.append(int(sys.stdin.readline()))
x.sort()

if c == 2:
    print(x[-1]-x[0])
else:
    c-=2
    l = 1
    r = x[-1]
    while l <= r:
        mid = (l+r)//2
        pre = x[0]
        s = 0
        for i in range(1,n-1):
            if x[i]-pre >= mid and x[-1]-x[i] >= mid:
                s+=1
                pre = x[i]
            if s > c:
                break
        if s>=c:
            l = mid+1
        else:
            r = mid-1
    print(r)
