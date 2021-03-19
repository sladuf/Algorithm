# 21.03.19 [탈출]

import sys
from collections import deque

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def water(w):
    w_temp=deque([])
    while w:
        x,y=w.popleft()
        for i in range(4):
            xx=dx[i]+x
            yy=dy[i]+y
            if 0<=xx<r and 0<=yy<c and m[xx][yy]=='.':
                m[xx][yy]='*'
                w_temp.append([xx,yy])
    return w_temp

def bfs(now):

    while q:
        if q[0][2] > now:
            break
        x,y,cnt=q.popleft()
        for i in range(4):
            xx=dx[i]+x
            yy=dy[i]+y
            if 0<=xx<r and 0<=yy<c and not visited[xx][yy]:
                if m[xx][yy]=='D':
                    return cnt+1
                if m[xx][yy] == '.':
                    visited[xx][yy]=True
                    q.append([xx,yy,cnt+1])
    return 0


r,c = map(int,sys.stdin.readline().split())
m=[]
for i in range(r):
    temp=list(sys.stdin.readline().strip())
    m.append(temp)

w=deque([])
q=deque([])
for i in range(r):
    for j in range(c):
        if m[i][j]=='S':
            q.append([i,j,0])
        if m[i][j]=='*':
            w.append([i,j])


res=0
now=0
visited=[[False]*c for x in range(r)]
while q:
    if res != 0:
        break
    w=water(w)
    res=bfs(now)
    now+=1
        

if res==0:
    print('KAKTUS')
else:
    print(res)

