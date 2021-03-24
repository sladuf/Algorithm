# 21.01.29 [정수 삼각형]
import sys

n=int(sys.stdin.readline())

dp = []
for i in range(n):
	temp = list(map(int, sys.stdin.readline().split()))
	dp.append(temp)

for i in range(1,n):
	for j in range(len(dp[i])):
		if j == 0:
			dp[i][j] += dp[i-1][j]
		elif j == len(dp[i])-1:
			dp[i][j] += dp[i-1][j-1]
		else:
			dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])
print(max(dp[n-1])) 
