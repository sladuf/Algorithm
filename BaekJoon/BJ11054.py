# 21.01.29 [가장 긴 바이토닉 부분 수열]
'''
무조건 반복문을 적게 쓴다고 좋은건 아니라는거!!!
'''
import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

dp = [[0,0] for i in range(n)]

for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dp[i][0] < dp[j][0]+1 :
            dp[i][0] = dp[j][0]+1
result = []
for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if a[i] > a[j] and dp[i][1] < dp[j][1]+1 :
            dp[i][1] = dp[j][1]+1
    result.append(sum(dp[i]))

print(max(result)+1)
