# 23.06.19
# 로봇 청소기

import sys

n,m = map(int, sys.stdin.readline().split(" "))
r,c,d = map(int, sys.stdin.readline().split(" "))
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split(" "))))

xy = [[-1,0],[0,1],[1,0],[0,-1]]
answer = 0
while True:
    if arr[r][c] == 0:
        arr[r][c] = -1
        answer+=1
    flag = False
    for i in range(4):
        d-=1
        if d < 0:
            d = 3
        if arr[r+xy[d][0]][c+xy[d][1]] == 0:
            r += xy[d][0]
            c += xy[d][1]
            flag = True
            break
    if flag:
        continue
    else:
        temp = (d+2)%4
        if arr[r+xy[temp][0]][c+xy[temp][1]] == 1:
            print(answer)
            break
        else:
            r += xy[temp][0]
            c += xy[temp][1]
