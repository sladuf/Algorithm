# 21.03.02 [타일 채우기]

'''
홀 수 일 때는 타일을 채울 수 없음!!
짝 수 일때는 예외의 경우가 있음 (4이상 부터 새로운 모양이 2종류 생겨남)

'''

import sys

n = int(sys.stdin.readline())
if n%2 == 1:
	print(0)
else:
	dp = [0 for x in range(n+1)]
	dp[2] = 3
	for i in range(4, n+1, 2):
		#2의 종류 3가지와 곱해준다.
		dp[i] = 3*dp[i-2]
		#4이상부터 새로운 모양이 2종류 생기기 때문에 2*dp
		for j in range(4, i, 2):
			dp[i] += 2*dp[i-j]
		#새로운 종류가 2가지 생김
		dp[i]+=2
		
	print(dp[n])
