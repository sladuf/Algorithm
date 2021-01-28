# 21.01.27 [벽 부수고 이동하기]
from collections import deque

dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]
def sol():
    ck = [[[0]*2 for _ in range(M)] for _ in range(N)]
    ck[0][0][0] = 1
    while q:
        x, y, wall = q.popleft()
        if x==(N-1) and y==(M-1): return ck[x][y][wall]
        for i in range(4):
            if 0 <= x+dx[i] < N and 0 <= y+dy[i] < M and ck[x+dx[i]][y+dy[i]][wall] == 0:
                if Map[x+dx[i]][y+dy[i]]=='0':
                    ck[x+dx[i]][y+dy[i]][wall] = ck[x][y][wall] + 1
                    q.append([x+dx[i], y+dy[i], wall])
                if wall == 0 and Map[x+dx[i]][y+dy[i]] == '1':
                    ck[x+dx[i]][y+dy[i]][1] = ck[x][y][0] + 1
                    q.append([x+dx[i], y+dy[i], 1])
    return -1

N, M = map(int, input().split())
Map = [list(input()) for _ in range(N)]
q = deque()
q.append([0, 0, 0])
print(sol())