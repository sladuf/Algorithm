# 설탕 배달
# 2023.05.05

import sys
input = sys.stdin.readline

def solutaion(n):
    if n == 3:
        return 1
    if n == 4:
        return -1
    
    dp = [0 for _ in range(n+1)]
    dp[3] = 1
    dp[5] = 1
    for i in range(6, n+1):
        if dp[i-3] == 0 and dp[i-5] == 0:
            continue
        elif dp[i-3] == 0:
            dp[i] = dp[i-5] +1
        elif dp[i-5] == 0:
            dp[i] = dp[i-3] +1
        else:
            dp[i] = min(dp[i-3], dp[i-5])+1
    
    return dp[n] if dp[n] > 0 else -1

n = int(input())
print(solutaion(n))

# 0일 때는 무시하고, min(n-3, n-5) +1