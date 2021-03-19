# 21.03.08 [합이 0인 네 정수]
'''
드디어 통과...이틀 걸렸다.
딕셔너리로 중복된 값의 횟수를 count해서 쉽게 구현하려고 했지만
시간초과가 나서 결국 while문으로 중복된 값의 횟수를 세어줄 수 밖에 없었다.
while문을 사용하는 것이 dic보다 빠르다니... 새로운 사실이다..^^

같은 유형 : 1208
'''
import sys

n=int(sys.stdin.readline())

A,B,C,D=[],[],[],[]
for i in range(n):
    a,b,c,d=map(int, sys.stdin.readline().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

ab=[]
cd=[]
for i in range(n):
    for j in range(n):
        ab.append(A[i]+B[j])
        cd.append(C[i]+D[j])

ab.sort()
cd.sort()
res=0
l=0
r=len(cd)-1
while l<len(ab) and r>=0:
    if ab[l]+cd[r]>0:
        r-=1
    elif ab[l]+cd[r]<0:
        l+=1
    else:
        a=1
        b=1
        while l<len(ab)-1 and ab[l+1]==ab[l]:
            l+=1
            a+=1
        while r>0 and cd[r-1]==cd[r]:
            r-=1
            b+=1
        res+=(a*b)
        l+=1
        r-=1

print(res)
