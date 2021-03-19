# 21.03.12 [보물섬]
'''
bf인것 같을 때 쫄지만 않으면 쉽게 풀린다는 교훈을 얻음
python3로는 시간초과나고 pypy3로 통과
'''

import sys
from collections import deque

dx=[0,0,1,-1]
dy=[1,-1,0,0]
def bfs(x,y):
    res=0
    visited=[[False]*m for x in range(n)]
    visited[x][y]=True
    q=deque([[x,y,0]])
    while q:
        x,y,cnt=q.popleft()
        res=max(res,cnt)
        for i in range(4):
            xx=dx[i]+x
            yy=dy[i]+y
            if 0<=xx<n and 0<=yy<m and not visited[xx][yy] and land[xx][yy]=='L':
                visited[xx][yy]=True
                q.append([xx,yy,cnt+1])
    return res

n,m=map(int,sys.stdin.readline().split())
land=[]
for i in range(n):
    land.append(list(sys.stdin.readline().strip()))

res=0
for i in range(n):
    for j in range(m):
        if land[i][j]=='L':
            temp=bfs(i,j)
            res=max(res,temp)
print(res)