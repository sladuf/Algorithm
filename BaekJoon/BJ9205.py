# 맥주 마시면서 걸어가기
# 2023.05.03

import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    start = list(map(int, input().split(" ")))
    temp = []
    for _ in range(n):
        temp.append(list(map(int, input().split(" "))))
    end = list(map(int, input().split(" ")))

    q = deque()
    q.append(start)
    visited = [False for _ in range(n)]
    flag = False
    while q:
        x,y = q.popleft()
        if abs(end[0]-x) + abs(end[1]-y) <= 1000:
            flag = True
            break
        else:
            for i in range(n):
                if abs(temp[i][0]-x) + abs(temp[i][1]-y) <= 1000 and visited[i] == False:
                    q.append(temp[i])
                    visited[i] = True
    if flag : print("happy")
    else: print("sad")