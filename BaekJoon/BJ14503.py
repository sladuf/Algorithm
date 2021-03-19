# 21.02.13 [로봇 청소기]
import sys
n,m = map(int, sys.stdin.readline().split())

r,c,d = map(int, sys.stdin.readline().split())

room = []
for i in range(n):
    room.append(list(map(int, sys.stdin.readline().split())))

result = 0
xy = [[-1,0],[0,-1],[1,0],[0,1]]
if d==1: d=3
elif d==3: d=1
while True:
    if room[r][c] == 0:
        result+=1
        room[r][c] = -1
    flag = False #갈곳있음?
    for i in range(4):
        d+=1
        if d==4:
            d=0
        x,y = xy[d]
        if i==1:
            wall = [r+x,c+y]
        if room[r+x][c+y] == 0:
            flag = True
            r +=x
            c +=y
            break
    if flag == False:
        if room[wall[0]][wall[1]] == 1:
            break
        else:
            r,c = wall

print(result)