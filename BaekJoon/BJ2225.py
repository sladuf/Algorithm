# 21.03.02 [합분해]
'''
0부터 n까지 만드는 방법을 모두 구해서 규칙을 찾음
규칙 : 
k/n 0 1 2 3 4 5
 1  1 1 1 1 1 1
 2  1 2 3 4 5 6
 3  1 3 6 10 15 21
한 칸 앞에 방법 + 한 칸 위에 방법
'''
import sys

n,k = map(int,sys.stdin.readline().split())

#k : 1~k까지
#n : 0~n까지의 경우를 모두 구함
dp = [[1]*(n+1) for x in range(k)]

for i in range(1,k):
	for j in range(1,n+1):
		dp[i][j] = (dp[i-1][j] + dp[i][j-1])%1000000000
		
print(dp[k-1][n])
