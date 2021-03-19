# 21.02.13 [포도주 시식]
import sys

n = int(sys.stdin.readline())

p = [0]
for i in range(n):
    p.append(int(sys.stdin.readline()))
if n == 1:
    print(p[1])
else:
    dp = [0,p[1],p[1]+p[2]]
    for i in range(3, n+1):
        dp.append(max(dp[i-3]+p[i]+p[i-1], dp[i-2]+p[i], dp[i-1]))

    print(dp[-1])
