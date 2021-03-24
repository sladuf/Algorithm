# 21.02.24 [치즈]
'''
구멍 체크하는 방법 고민하다가 시간 다 간 문제,,
결론 : [0,0]은 무조건 0임
그러니까 여기서부터 bfs로 인접한 1을 찾아서 녹이면 댐
(한 번 녹이고 다시 [0,0]부터 녹이고...)
인접한 0만 q에 담으니까 구멍의 0은 인접하지 않아서 담지 않게됨
'''
import sys
from collections import deque

def bfs():
	visited = [[True]*m for x in range(n)]
	dx = [1,-1,0,0]
	dy = [0,0,1,-1]
	q = deque([[0,0]])
	res = 0
	#0만 q에 담아
	while q:
		x,y = q.popleft()
		for i in range(4):
			xx = x+dx[i]
			yy = y+dy[i]
			if 0<=xx<n and 0<=yy<m:
				#인접한 1은 0으로 바꿔주고 방문표시를 해준다!
				if ch[xx][yy] == 1:
					res +=1
					ch[xx][yy] = 0
					visited[xx][yy] = False
				elif visited[xx][yy]:
					q.append([xx,yy])
					visited[xx][yy] = False

	#res는 녹은 1을 return함 (마지막으로 녹은 1을 찾기위한 여정)
	return res
	

n,m = map(int, sys.stdin.readline().split())

ch = []
for i in range(n):
	ch.append(list(map(int, sys.stdin.readline().split())))

time = 0
last = 0
for i in range(n):
	for j in range(m):
		#어차피 [0,0]부터 검색한 1은 무조건 녹으니까...
		if ch[i][j] == 1:
			last = bfs()
			time+=1
print(time)
print(last)
