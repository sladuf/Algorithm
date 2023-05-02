# 소가 길을 건너간 이유 6
# 2023.05.02

import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

n,k,r = map(int, input().split(" "))
road = [[[] for _ in range(n)] for _ in range(n)]
for i in range(r):
    a,b,c,d = map(int, input().split(" "))
    road[a-1][b-1].append((c-1,d-1))
    road[c-1][d-1].append((a-1,b-1))

cows = []
for i in range(k):
    x,y = map(int, input().split(" "))
    cows.append([x-1,y-1])

dx = [0,0,1,-1]
dy = [1,-1,0,0]
result = 0
while cows:
    cow = cows.pop()
    visited = [[False]*n for _ in range(n)]
    q = deque()
    q.append(cow)
    visited[cow[0]][cow[1]] = True
    while q:
        x,y = q.popleft()
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            if xx<0 or xx>=n or yy<0 or yy>=n:
                continue
            print(xx,yy,x,y)
            if (xx,yy) in road[x][y] or (x,y) in road[xx][yy]:
                continue
            if visited[xx][yy]:
                continue
            visited[xx][yy] = True
            q.append([xx,yy])
    for a,b in cows:
        if not visited[a][b]:
            result+=1
print(result)
