# 21.01.28 [LCS]
'''
예전에 풀었던건데 몰라서 또 구글링...
너무 어려운 규칙 찾기 ㅠㅠ
'''
import sys

a = list(sys.stdin.readline().strip())
b = list(sys.stdin.readline().strip())

dp = [[0]*(len(a)+1) for i in range(len(b)+1)]

for i in range(1, len(b)+1):
    for j in range(1, len(a)+1):
        if b[i-1] == a[j-1]:
            dp[i][j] = dp[i-1][j-1] +1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
result = 0

for i in dp:
    result = max(result, max(i))
print(result)
