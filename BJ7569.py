# 21.02.19 [토마토]
from collections import deque
import sys

def bfs(q):
	global res
	dx = [0,0,0,0,1,-1]
	dy = [1,-1,0,0,0,0]
	dz = [0,0,1,-1,0,0]
	while q:
		a,b,c,cnt = q.popleft()
		for x in range(6):
			xx = a+dx[x]
			yy = b+dy[x]
			zz = c+dz[x]
			if 0 <= xx < h and 0 <= yy < n and 0 <=zz < m and tomato[xx][yy][zz] == 0:
				tomato[xx][yy][zz] = cnt+1
				q.append([xx,yy,zz,cnt+1])

m,n,h = map(int,sys.stdin.readline().split())
tomato = []
for i in range(h):
	t = []
	for j in range(n):
		temp = list(map(int, sys.stdin.readline().split()))
		t.append(temp)
	tomato.append(t)

q = deque([])
for i in range(h):
	for j in range(n):
		for k in range(m):
			if tomato[i][j][k] == 1:
				q.append([i,j,k,1])

bfs(q)
res = 0
flag = True
for i in range(h):
	for j in range(n):
		if 0 in tomato[i][j]:
			flag = False
			break
		res = max(res,max(tomato[i][j]))
	if flag == False:
		break
if flag == False:
	print(-1)
else:
	print(res-1)