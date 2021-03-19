# 21.01.26 [숫자판 점프]

import sys

dx = [0,0,1,-1]
dy = [1,-1,0,0]
def dfs(x,y, cnt):
    num = []
    if cnt == 6:
        num = [str(metrix[x][y])]
    else:
        num = []
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<5 and 0<=yy<5:
                temp = dfs(xx, yy, cnt+1)
                for i in range(len(temp)):
                    temp[i] = str(metrix[x][y]) + temp[i]
                num += temp
    return num

metrix = []
for i in range(5):
    temp = list(map(int, sys.stdin.readline().split()))
    metrix.append(temp)

result = set()
for a in range(5):
    for b in range(5):
        for value in set(dfs(a,b,1)):
            result.add(value)

print(len(result))