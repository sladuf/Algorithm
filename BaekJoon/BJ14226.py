# 2023.06.23
# 이모티콘
import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque()
# 0: 화면, 1: 클립보드
q.append([1,0])
visited = [[float("inf")]*2001 for _ in range(2001)]
visited[1][0] = 0

#if 화면 != 클립보드 -> 화면 -> 클립보드
#if 클립보드 0이 아니면 : 클립보드 -> 화면
#if 화면 0이 아니면 : 화면-1

while q:
    a,b = q.popleft()
    if a == n:
        print(visited[a][b])
        break
    cnt = visited[a][b]+1
    if a!=b and visited[a][a] > cnt:
        visited[a][a] = cnt
        q.append([a,a])
    if b!=0 and a+b <= 2000 and visited[a+b][b] > cnt:
        visited[a+b][b] = cnt
        q.append([a+b,b])
    if a!=0 and visited[a-1][b] > cnt:
        visited[a-1][b] = cnt
        q.append([a-1,b])

