# 21.01.28 [피보나치 함수]
import sys

t = int(sys.stdin.readline())

dp = [[0,0] for i in range(41)]
dp[0] = [1,0]
dp[1] = [0,1]

for i in range(2, 41):
	dp[i][0] = dp[i-1][0] + dp[i-2][0]
	dp[i][1] = dp[i-1][1] + dp[i-2][1]

for i in range(t):
	n = int(sys.stdin.readline())
	print(dp[n][0],dp[n][1])