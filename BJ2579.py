# 21.01.29 [계단 오르기]

import sys
n = int(sys.stdin.readline())
step = []
for i in range(n):
    step.append(int(sys.stdin.readline()))

if n == 1:
    print(step[0])
else:
    dp = [[x,x] for x in step]
    dp[1][1] += dp[0][1]

    for i in range(2, n):
        temp = max(dp[i-2])
        dp[i][0] += temp
        dp[i][1] += dp[i-1][0]

    print(max(dp[n-1]))