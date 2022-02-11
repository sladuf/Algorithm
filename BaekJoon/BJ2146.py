# 21.03.04 [다리 만들기]
'''
스스로 풀었다는 것에 의의를 두는 엉망진창 코드...
pypy로 간신히..통과했다!
섬에 각자 고유번호를 매겨주고 섬 하나마다 다른 섬으로 가는 경우를 bfs한다.
'''
import sys
from collections import deque
import copy

dx=[0,0,1,-1]
dy=[1,-1,0,0]

#land는 섬의 고유번호 해당 섬이 다른 섬을 만나는 경우를 check
#섬이 바다를 만나는 경우 바다를 land로 바꿔주고 경로 +1 한다.
#다른 섬을 만나면 경로의 횟수를 최소와 비교하고 return
def bfs(land,queue):
	global res

	cp = copy.deepcopy(t)
	while queue:
		x,y,cnt = queue.popleft()
		for i in range(4):
			xx=x+dx[i]
			yy=y+dy[i]
			if 0<=xx<n and 0<=yy<n :
				if cp[xx][yy] == 0:
					cp[xx][yy] = land
					queue.append([xx,yy,cnt+1])
				elif cp[xx][yy] != land:
					res=min(res,cnt)
					return

	return land 

#섬에 고유번호를 매겨주는 함수
#동시에 queue에 해당 섬을 넣는다.
def ch(x,y,land):
	q = deque([[x,y]])
	t[x][y] = land
	queue = deque([[x,y,0]])
	while q:
		x,y = q.popleft()
		for i in range(4):
			xx=dx[i]+x
			yy=dy[i]+y
			if 0<=xx<n and 0<=yy<n and t[xx][yy]==1:
				q.append([xx,yy])
				t[xx][yy]=land
				queue.append([xx,yy,0])
	return queue

n=int(sys.stdin.readline())

t = []
for i in range(n):
	t.append(list(map(int, sys.stdin.readline().split())))

res = n*n
land=2
for i in range(n):
	for j in range(n):
		if t[i][j] == 1:
			#섬이면 고유번호를 붙인 뒤에 bfs한당
			queue = ch(i,j,land)
			bfs(land,queue)
			land+=1

print(res)


