import sys
from collections import deque

def bfs(w):
	global res
	q = deque([[0,0,1]])
	dx = [0,0,1,-1]
	dy = [1,-1,0,0]
	while q:
		x,y,cnt= q.popleft()
		if x==(n-1) and y==(m-1):
			res.append(cnt)
			return
		for i in range(4):
			xx = x+dx[i]
			yy = y+dy[i]
			if 0<=xx<n and 0<=yy<m and w[xx][yy] == 0:
				w[xx][yy] = 1
				q.append([xx,yy,cnt+1])

n,m = map(int, sys.stdin.readline().split())
wall = []
for i in range(n):
	temp = list(sys.stdin.readline().strip())
	wall.append(list(map(int, temp)))

res = []
w = copy.deepcopy(wall)
bfs(w)
for i in range(n):
	for j in range(m):
		if wall[i][j] == 1:
			w = copy.deepcopy(wall)
			w[i][j] = 0
			bfs(w)
if res:
	print(min(res))
else:
	print(-1)
