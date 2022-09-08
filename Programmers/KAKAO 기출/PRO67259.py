# https://school.programmers.co.kr/learn/courses/30/lessons/67259

from collections import deque

dx=[1,-1,0,0]
dy=[0,0,1,-1]
def bfs(z,board):
    n=len(board)
    q=deque([])
    visited=[[0]*n for x in range(n)]
    visited[0][0]=1
    q.append([0,0,z,0])
    
    while q:
        x,y,z,cnt=q.popleft()
        if x==n-1 and y==n-1:
            res.append(cnt)
            continue
        for i in range(4):
            xx=dx[i]+x
            yy=dy[i]+y
            if 0<=xx<n and 0<=yy<n and board[xx][yy]==0:
                if z<=1 and i<=1:
                    move=cnt+100
                elif z>=2 and i>=2:
                    move=cnt+100
                else:
                    move=cnt+600
                    
                if visited[xx][yy]==0 or visited[xx][yy]>move:
                    visited[xx][yy]=move
                    q.append([xx,yy,i,move])

def solution(board):
    global res
    res=[]
    bfs(2,board)
    bfs(0,board)
    return min(res)