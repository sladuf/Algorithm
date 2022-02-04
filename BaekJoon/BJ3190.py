# 22.02.03 [뱀]

import sys
from collections import deque

'''
아무것도 없으면 0
사과 있으면 1
뱀이 있으면 2

오른쪽 "D"
왼쪽 "L"
'''

n = int(sys.stdin.readline())
metrix = [ [0]*n for x in range(n) ]

k = int(sys.stdin.readline())
for i in range(k):
    a,b = map(int, sys.stdin.readline().split())
    metrix[a-1][b-1] = 1

move = deque([])
l = int(sys.stdin.readline())
for i in range(l):
    a,b = sys.stdin.readline().split()
    move.append([int(a), b])

x,y = 0,0
dx = [0,1,0,-1]
dy = [1,0,-1,0]
index = 0
loc = "D"

bam = deque([[0,0]])
time = 1
while True:
    x += dx[index]
    y += dy[index]
    

    if 0<= x < n and 0<= y < n and metrix[x][y] != 2:
        if metrix[x][y] == 1:
            metrix[x][y]=2
            bam.appendleft([x,y])
        else:
            metrix[x][y]=2
            bam.appendleft([x,y])
            delx,dely = bam.pop()
            metrix[delx][dely] = 0
    else:
        break

    #회전 여부
    if move and move[0][0] == time:
        loc = move[0][1]
        if loc == "L":
            index = (index-1)%4
        else:
            index = (index+1)%4
        move.popleft()
    time+=1

print(time)
