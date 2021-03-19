# 21.01.25 [연결 요소의 개수]

from collections import deque
import sys

def bfs(v):
    queue = deque([v])
    visited[v] = 1
    while queue:
        pop = queue.popleft()
        while graph[pop]:
            temp = graph[pop].pop()
            if visited[temp] == 0:
                queue.append(temp)
                visited[temp] = 1


n, m = map(int, sys.stdin.readline().split())

graph = [[] for x in range(n+1)]
visited = [0] * (n+1)

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

result = 0

for i in range(1, n+1):
    if visited[i] == 0:
        bfs(i)
        result+=1

print(result)
