# 22.02.20 [오르막 수]

'''
1 1 1 1 1 1 1 1 1 1
10 9 8 7 6 5 4 3 2 1
'''
import sys

n = int(sys.stdin.readline())
dp=[[1]*10 for i in range(n+1)]
for i in range(2, n+1):
	for j in range(8,-1,-1):
		dp[i][j] = dp[i][j+1] + dp[i-1][j]

print(sum(dp[n])%10007)