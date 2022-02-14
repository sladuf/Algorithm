# 22.02.15 [2xN 타일링]

import sys

n = int(sys.stdin.readline())
'''
2x1 : 세로1
2x2 : 세로1+세로1, 가로2
(가로2는 한쌍으로 움직여야해)
2x3 : 2x1 + 가로2, 2x2 + 세로1
'''
dp = [0] * (n+1)
dp[0] = 1
dp[1] = 1
for i in range(2, n+1):
    dp[i] += (dp[i-1] + dp[i-2])%10007

print(dp[n])