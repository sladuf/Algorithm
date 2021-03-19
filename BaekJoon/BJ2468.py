# 21.01.25 [안전 영역]

import sys
from collections import deque

def dfs(x,y, i):
    queue = deque([[x,y]])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue:
        x, y = queue.popleft()
        for ii in range(4):
            xx = dx[ii] + x
            yy = dy[ii] + y
            if 0<=xx<n and 0<=yy<n and visited[xx][yy] ==0 and metrix[xx][yy] > i:
                queue.append([xx, yy])
                visited[xx][yy] = 1


n = int(sys.stdin.readline())
max_num = 0
metrix = []
result = []

for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    metrix.append(temp)
    if max_num < max(temp): max_num = max(temp)

for i in range(max_num):
    visited = [[0]*n for x in range(n)]
    cnt = 0
    for a in range(n):
        for b in range(n):
            if metrix[a][b] > i and visited[a][b] == 0:
                visited[a][b] = 1
                dfs(a,b, i)
                cnt +=1
    result.append(cnt)

print(max(result))