# 21.02.25 [카드 구매하기]
import sys
n = int(sys.stdin.readline())
p = [0]+list(map(int, sys.stdin.readline().split()))
 
dp = [0 for x in range(n+1)]

for i in range(len(p)):
	for j in range(i,n+1):
		dp[j] = max(dp[j],p[i]+dp[j-i])

print(dp[-1])
