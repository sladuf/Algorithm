# 21.01.26 [양 한마리... 양 두마리...]
import sys
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(x, y):
    queue= deque([[x, y]])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            xx = dx[i]+x
            yy = dy[i]+y
            if 0<=xx<h and 0<=yy<w and grid[xx][yy] == "#":
                queue.append([xx, yy])
                grid[xx][yy] = '.'


t = int(sys.stdin.readline())
for i in range(t):
    h, w = map(int, sys.stdin.readline().split())
    grid = []
    result = 0
    for i in range(h):
        temp = list(sys.stdin.readline().strip())
        grid.append(temp)
    for a in range(h):
        for b in range(w):
            if grid[a][b] == "#":
                grid[a][b] = '.'
                bfs(a, b)
                result+=1

    print(result)