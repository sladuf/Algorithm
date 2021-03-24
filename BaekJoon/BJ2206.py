# 21.01.27 [벽 부수고 이동하기]
import sys
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    wall[0][0][0] = 1
    queue = deque([[0,0,0]])
    while queue:
        x, y, z = queue.popleft()
        if x ==(n-1) and y==(m-1) : return wall[x][y][z]
        for i in range(4):
            xx=dx[i]+x
            yy=dy[i]+y
            if 0<=xx<n and 0<=yy<m and wall[xx][yy][z] == 0:
                if mapp[xx][yy] == 0:
                    wall[xx][yy][z] = wall[x][y][z]+1
                    queue.append([xx,yy,z])
                elif z==0:
                    wall[xx][yy][1] = wall[x][y][0]+1
                    queue.append([xx,yy,1])

n,m = map(int, sys.stdin.readline().split())

mapp = []
for i in range(n):
    temp = list(sys.stdin.readline().strip())
    mapp.append(list(map(int, temp)))

wall = [[[0]*2 for x in range(m)] for x in range(n)]
result = bfs()

if result: print(result)
else: print(-1)
