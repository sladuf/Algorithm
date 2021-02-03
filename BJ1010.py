# 21.02.03 [다리 놓기]
import sys

def mCn(m,n):
	if dp[m][n] != 0:
		return dp[m][n]
	elif n == 0:
		dp[m][n] = 1
		return 1
	elif n == m:
		dp[m][n] = 1
		return 1
	elif n == 1:
		dp[m][n] = m
		return m
	else:
		dp[m][n] = mCn(m-1,n) + mCn(m-1,n-1)
		return dp[m][n]

t = int(sys.stdin.readline())
dp = [[0]*30 for i in range(30)]
for i in range(t):
	n,m = map(int, sys.stdin.readline().split())
	result = mCn(m,n)
	print(result)