# 22.02.14 [1,2,3 더하기]

import sys
t = int(sys.stdin.readline())
'''
1 : 1
2 : 1+1, 2
3 : 1+1+1, 1+2, 2+1, 3
'''
dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4,11):
    dp[i] += dp[i-1]
    dp[i] += dp[i-2]
    dp[i] += dp[i-3]

for i in range(t):
    n = int(sys.stdin.readline())
    print(dp[n])