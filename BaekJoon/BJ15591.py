# MooTube
# 2023.05.02
# BFS
# pypy3로 제출

import sys
from collections import defaultdict
from collections import deque

input = sys.stdin

n,q = map(int, input.readline().split(" "))
dic = defaultdict(list)
for i in range(n-1):
    a,b,c = map(int, input.readline().split(" "))
    dic[a].append([b,c])
    dic[b].append([a,c])
for i in range(q):
    k,v = map(int, input.readline().split(" "))
    visited = [False for _ in range(n+1)]
    queue = deque()
    queue.append([v,1_000_000_000])
    visited[v] = True
    result = 0
    while queue:
        now, cnt = queue.popleft()
        for node,edge in dic[now]:
            if visited[node]:
                continue
            if min(cnt, edge) >= k:
                result+=1
            visited[node] = True
            queue.append([node, min(cnt,edge)])
    print(result)



