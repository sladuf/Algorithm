# 21.01.27 [토마토]
import sys
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def dfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            xx = dx[i]+x
            yy = dy[i]+y
            if 0<=xx<n and 0<=yy<m and tomato[xx][yy] != -1:
                if tomato[xx][yy] == 0 or tomato[xx][yy] > (tomato[x][y]+1):
                    tomato[xx][yy] = tomato[x][y]+1
                    queue.append([xx,yy])

m,n = map(int, sys.stdin.readline().split())

tomato = []
for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    tomato.append(temp)

queue = deque([])
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append([i,j])
dfs()
result = 0
for i in tomato:
    if 0 in i:
        result = -1
        break
        
if result == -1:
    print(-1)
else:
    print(max(map(max, tomato))-1)
