# 21.01.27 [케빈 베이컨의 6단계 법칙]
def bfs(me):
    visited = [0 for i in range(n+1)]
    queue = deque([[me, 0]])
    visited[me] = 1
    while queue:
        you, cnt = queue.popleft()
        cnt +=1
        for t in friends[you]:
            if visited[t] == 0:
                visited[t] = cnt
                queue.append([t, cnt])
    return visited

import sys
from collections import deque
from collections import defaultdict

n,m = map(int, sys.stdin.readline().split())

friends = defaultdict(list)
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    friends[a].append(b)
    friends[b].append(a)

result = []
for i in range(1, n+1):
    temp = bfs(i)
    temp2 = 0
    for j in range(1,n+1):
        if i == j : continue
        temp2+=temp[j]
    result.append(temp2)

s = 0
for i in range(n):
    if result[s] > result[i]:
        s = i
print(s+1)
