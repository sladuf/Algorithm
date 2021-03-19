# 21.01.25 [연구소]

import sys
from itertools import combinations
import copy
from collections import deque

def safe(r_copy):
    cnt = 0
    for i in range(n):
        cnt += r_copy[i].count(0)
    result.append(cnt)

def bfs(wall, room):
    r_copy = copy.deepcopy(room)
    for a, b in wall:
        r_copy[a][b] = 1
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    queue = deque([])
    for c in range(n):
        for d in range(m):
            if r_copy[c][d] == 2:
                queue.append([c,d])
    while queue:
        temp_x, temp_y = queue.popleft()
        for i in range(4):
            xx = temp_x + dx[i]
            yy = temp_y + dy[i]
            if 0<=xx<n and 0<=yy<m and r_copy[xx][yy] == 0:
                r_copy[xx][yy] = 2
                queue.append([xx,yy])
    safe(r_copy)

n,m = map(int ,sys.stdin.readline().split())
room = []
result = []

for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    room.append(temp)

zero= []
for x in range(n):
    for y in range(m):
        if room[x][y] == 0:
            zero.append([x,y])

for i in list(combinations(zero, 3)):
    bfs(i, room)
print(max(result))