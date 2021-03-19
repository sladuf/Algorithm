# 21.01.28 [오르막 수]
'''
10844 [쉬운 계단 수] 풀고나서 풀어서 쉽게 풀 수 있었당 (운빨이란 소리)
'''
import sys

n = int(sys.stdin.readline())
dp = [[1]*10 for y in range(n+1)]
for i in range(2, n+1):
	for j in range(1, 10):
		dp[i][j] = dp[i-1][j] + dp[i][j-1]

result = sum(dp[n])
print(result%10007)