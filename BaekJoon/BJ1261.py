# 21.03.08 [알고스팟]
'''
이동하면서 벽을 부순 횟수를 저장 : 이차원 리스트 v
상하좌우로 이동하며 이미 방문한 곳이라도 벽을 부순 횟수가 더 적으면 또 방문하여 횟수를 갱신(최솟값으로)
마지막 점 까지 방문 하고, 더 이상 더 적은 횟수가 존재하지 않으면 그만함
'''
import sys
from collections import deque

m,n=map(int,sys.stdin.readline().split())

miro=[]
for i in range(n):
	miro.append(list(map(int,list(sys.stdin.readline().strip()))))

#해당 칸에 도착했을 때 벽을 부순 횟수를 저장
#해당 칸을 지난 적이 없으면 -1
v=[[-1]*m for x in range(n)]
v[0][0]=0
dx=[1,-1,0,0]
dy=[0,0,1,-1]
q=deque([[0,0]])
while q:
	x,y=q.popleft()
	for i in range(4):
		xx=dx[i]+x
		yy=dy[i]+y
		if 0<=xx<n and 0<=yy<m:
			#지나온 적이 없으면 일단 지나가
			if v[xx][yy]==-1:
				v[xx][yy]=v[x][y]+miro[xx][yy]
				q.append([xx,yy])
			#이미 지나갔지만 벽을 부순 횟수를 더 줄일 수 있다면 다시 방문
			elif v[xx][yy]>v[x][y]+miro[xx][yy]:
				v[xx][yy]=v[x][y]+miro[xx][yy]
				q.append([xx,yy])
				
print(v[n-1][m-1])
