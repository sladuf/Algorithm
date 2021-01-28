# 21.01.26 [섬의 개수]
import sys
from collections import deque

def search_island(mapp):
    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, 1, -1, 1, -1]
    island = 0
    for a in range(w):
        for b in range(h):
            if mapp[b][a] == 1:
                queue = deque([[b,a]])
                mapp[b][a] = 0
                island +=1
                while queue:
                    x, y = queue.popleft()
                    for i in range(8):
                        xx = x+dx[i]
                        yy = y+dy[i]
                        if 0<=xx<h and 0<=yy<w and mapp[xx][yy] == 1:
                            queue.append([xx,yy])
                            mapp[xx][yy] = 0
    return island


while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0 :
        break

    mapp = []
    for i in range(h):
        temp = list(map(int, sys.stdin.readline().split()))
        mapp.append(temp)

    result = search_island(mapp)
    print(result)