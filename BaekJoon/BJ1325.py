# 21.02.01 [효율적인 해킹]
'''
하나도 안 효율적인 느낌...
'''
import sys
from collections import deque, defaultdict

def bfs(i):
	cnt = 0
	visited = [0 for x in range(n+1)]
	visited[i] = 1
	queue = deque([i])
	while queue:
		temp = queue.popleft()
		for t in dic[temp]:
			if visited[t] == 0:
				visited[t] = 1
				cnt +=1
				queue.append(t)
	return cnt

n,m=map(int, sys.stdin.readline().split())

dic = defaultdict(list)
for i in range(m):
	a,b = map(int,sys.stdin.readline().split())
	dic[b].append(a)

result = [0 for x in range(n+1)]
for i in range(1, n+1):
	result[i] = bfs(i)

temp = max(result)
for i in range(n+1):
	if result[i] == temp:
		print(i, end=' ')
