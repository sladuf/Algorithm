# 21.02.23 [소수의 연속합]
'''
소수를 찾아 놓고 two-pointer
'''
import sys
n = int(sys.stdin.readline())

dp = [1 for x in range(n+1)]
dp[0] = 0
dp[1] = 0

sosu = []
for i in range(2,n+1):
	if dp[i] == 1:
		sosu.append(i)
		for i in range(i*i, n+1, i):
			dp[i] = 0

if n == 1:
	print(0)
else:
	l = 0
	r = 1
	total = sosu[0]
	#자기자신이 소수면 결과값 1부터 시작
	if sosu[-1] == n:
		res =1
	else:
		res = 0
	while l<=r<len(sosu):
		#값이 작으면 r값 오른쪽으로 이동
		if total<n:
			total += sosu[r]
			r+=1
		else:
		#값이 같거나 작으면 l값 오른쪽으로 이동
			if total == n:
				res+=1
			total -= sosu[l]
			l +=1

	print(res)