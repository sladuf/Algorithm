# 21.02.23 [골드바흐의 추측]
import sys

dp = [1 for x in range(1000001)]
dp[0] = 0
dp[1] = 0
sosu = []
for i in range(2,1000001):
    if dp[i] == 1:
        sosu.append(i)
        for i in range(i*i, 1000001, i):
            dp[i] = 0

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    l = 1
    r = 1
    #sosu에서 n보다 작은 소수만을 가지게 하기 위해 r을 check
    for i in range(len(sosu)):
        if sosu[i] > n:
            r = i-1
            break

    #6=3+3이라서 while에 등호가 필요함!!!
    while l<=r:
        if sosu[l] + sosu[r] == n:
            print(n,"=",sosu[l],"+",sosu[r])
            break
        elif sosu[l] + sosu[r] > n:
            r-=1
        else:
            l+=1
    if l>r:
        print("Goldbach's conjecture is wrong.")