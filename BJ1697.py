# 21.02.01 [숨바꼭질]
import sys
from collections import deque

n,k = map(int, sys.stdin.readline().split())

queue = deque([[n,0]])
result = 0
visited = [False for i in range(100001)]
while queue:
	temp, spot = queue.popleft()
	if temp == k :
		result = spot
		break
	elif not visited[temp]:
		visited[temp] = True
		if temp-1 >= 0:
			queue.append([temp-1,spot+1])
		if temp+1 <= 100000:
			queue.append([temp+1,spot+1])
		if temp*2 <= 100000:
			queue.append([temp*2,spot+1])

print(result)