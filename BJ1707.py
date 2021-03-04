# 21.03.04 [이분 그래프]
import sys
from collections import defaultdict
from collections import deque

'''
visited라는 그룹 두개를 만들어
내가 속한 곳에 나랑 연결되어 있는 정점이 있다면 False
'''
now = 0
def bfs(n):
	global now
	q = deque([[n,now]])
	visited[now][n] = True
	while q:
		a,b = q.popleft()
		if b == 0:
			now = 1
		else:
			now = 0
		for i in dic[a]:
			if visited[b][i]:
				return False
			elif not visited[now][i]:
				q.append([i,now])
				visited[now][i] = True
	return True


t = int(sys.stdin.readline())

for case in range(t):
	v,e = map(int, sys.stdin.readline().split())
	dic = defaultdict(list)
	for i in range(e):
		a,b = map(int, sys.stdin.readline().split())
		dic[a].append(b)
		dic[b].append(a)

	flag = True
	visited = [[False]*(v+1) for x in range(2)]
	for i in dic.keys():
		if visited[now][i] == False and visited[now-1][i] == False:
			flag = bfs(i)
			if flag == False:
				break

	if flag:
		print('YES')
	else:
		print('NO')
