# 21.01.29 [이친수]
import sys

n = int(sys.stdin.readline())

dp = [1 for i in range(n)]

for i in range(2, n):
	dp[i] = dp[i-1]+dp[i-2]
print(dp[n-1])
