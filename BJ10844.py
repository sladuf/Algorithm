# 21.01.28 [쉬운 계단 수]

'''
규칙 도저히 생각이 안나!!!! 그래서 구글링함
  0 1 2 3 4 5 6 7 8 9 자릿수 / 입력가능한 갯수
1 0 1 1 1 1 1 1 1 1 1 = 9
2 1 1 2 2 2 2 2 2 2 1 = 17
3 1 3 3 4 4 4 4 4 3 2 = 32
뭐 이런식으로..
'''
import sys

n = int(sys.stdin.readline())
dp = [[1]*10 for i in range(n+1)]
dp[1][0] = 0
for i in range(2, n+1):
    for j in range(0, 10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
result = sum(dp[n])
print(result%1000000000)
