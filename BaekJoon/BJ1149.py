# 21.01.29 [GRB거리]

import sys
n = int(sys.stdin.readline())
cost = []
for i in range(n):
	temp = list(map(int, sys.stdin.readline().split()))
	cost.append(temp)

for i in range(1, n):
	cost[i][0] += min(cost[i-1][1], cost[i-1][2])
	cost[i][1] += min(cost[i-1][0], cost[i-1][2])
	cost[i][2] += min(cost[i-1][0], cost[i-1][1])

print(min(cost[n-1]))
