# 21.03.02 [제곱수의 합]
'''
1부터 n까지의 제곱수의 합을 구한다.
dp에 1부터 n까지 제곱수 합의 최소값 저장
'''
import sys

n = int(sys.stdin.readline())

#젤 처음은 1의 합으로 초기화 (최댓값)
dp = [x for x in range(n+1)]

for i in range(1,n+1):
	for j in range(1,i):
		if j**2 > i:
			break

		#현재 숫자에서 제곱수의 합의 최소를 구함
		dp[i] = min(dp[i], dp[i-j**2]+1)

print(dp[n])