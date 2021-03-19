# 21.01.25 [유기농 배추]

from collections import deque


def bfs(y, x):
    l_dx = [0, 0, 1, -1]
    l_dy = [1, -1, 0, 0]

    queue = deque([[y,x]])
    while queue:
        yy, xx = queue.popleft()
        for p in range(4):
            dx = xx + l_dx[p]
            dy = yy + l_dy[p]
            if 0 <= dx < m and 0 <= dy < n and metrix[dy][dx] == 1:
                    queue.append([dy, dx])
                    metrix[dy][dx] = 0

t = int(input())

for i in range(t):
    result = 0
    m, n, k = map(int, input().split())
    metrix = [[0]*m for x in range(n)]

    for j in range(k):
        x, y = map(int, input().split())
        metrix[y][x] = 1

    for x in range(m):
        for y in range(n):
            if metrix[y][x] == 1:
                metrix[y][x] = 0
                bfs(y, x)
                result +=1
    print(result)