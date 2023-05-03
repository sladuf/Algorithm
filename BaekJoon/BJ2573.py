# 빙산
# 2023.05.03

import sys
from collections import deque
import copy

def find(nm):
    q = deque()
    flag = False
    for i in range(len(nm)):
        for j in range(len(nm[0])):
            if nm[i][j] > 0:
                q.append((i,j))
                flag = True
                break
        if flag: break
    
    if len(q) == 0:
        return -1
    
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    visited = [[False]*len(nm[0]) for _ in range(len(nm))]
    visited[q[0][0]][q[0][1]] = True
    while q:
        x,y = q.popleft()
        for i in range(4):
            xx = dx[i]+x
            yy = dy[i]+y
            if 0<=xx<len(nm) and 0<=yy<len(nm[0]) and nm[xx][yy] > 0 and visited[xx][yy] == False:
                visited[xx][yy] = True
                q.append((xx,yy))

    for i in range(len(nm)):
        for j in range(len(nm[0])):
            if nm[i][j] > 0 and visited[i][j] == False:
                return 1
    return 0

input = sys.stdin.readline

n,m = map(int, input().split(" "))
nm = []
for _ in range(n):
    nm.append(list(map(int, input().split(" "))))

year = 0
while True:
    #두 덩이 이상으로 분리되었는지 확인
    #-1전체가 녹은경우 1두덩이 0분리X
    temp = find(nm)
    if temp == 1:
        print(year)
        break
    elif temp == -1:
        print(0)
        break
    
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    #빙산 찾아서 줄이기
    newnm = copy.deepcopy(nm)
    for x in range(n):
        for y in range(m):
            if nm[x][y] > 0:
                cnt = 0
                for i in range(4):
                    xx = dx[i]+x
                    yy = dy[i]+y
                    if 0<=xx<n and 0<=yy<m and nm[xx][yy] == 0:
                        cnt+=1
                newnm[x][y] = nm[x][y]-cnt if nm[x][y]-cnt>0 else 0
    nm = newnm
    year+=1

