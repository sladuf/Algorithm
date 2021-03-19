# 21.02.23 [가로수]
'''
가로수 간격들의 최대공약수 만큼 간격을 두고 나무를 심는다.
'''
import sys

def gcd(a,b):
    if a < b :
        a,b = b,a
    while a%b:
        a,b = b,a%b
    return b

n = int(sys.stdin.readline())
t = []
for i in range(n):
    t.append(int(sys.stdin.readline()))
t.sort()

g = t[1]-t[0]
for i in range(2, n):
    g = gcd(g, t[i]-t[i-1])

res = 0
for i in range(1,n):
    #간격 -1이 심을 나무 수
    res += (t[i]-t[i-1])//g -1
print(res)