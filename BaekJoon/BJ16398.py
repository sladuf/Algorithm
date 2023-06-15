# 2023.06.15
# 행성 연결

import sys
import heapq

n = int(sys.stdin.readline())
flow = []
for _ in range(n):
    temp = list(map(int, sys.stdin.readline().split(" ")))
    flow.append(temp)

answer = 0

visited = [False for _ in range(n)]
visited[0] = True
heap = []
for i in range(n):
    if i == 0:
        continue
    heapq.heappush(heap, [flow[0][i], i])

while heap:
    f,c = heapq.heappop(heap)
    if visited[c]:
        continue
    visited[c] = True
    answer += f
    for i in range(n):
        if visited[i]:
            continue
        heapq.heappush(heap, [flow[c][i], i])

print(answer)