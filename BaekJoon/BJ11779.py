import sys
import heapq
from collections import defaultdict

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
bus = defaultdict(list)

for i in range(m):
    a,b,c = map(int, sys.stdin.readline().split(" "))
    bus[a].append([b,c])

st,end = map(int, sys.stdin.readline().split(" "))

totalLoad = [st]

edge = [[float("inf"),0] for _ in range(n+1)]
edge[st][0] = 0
heap = [(0,st)]

while heap:
    cost, node = heapq.heappop(heap)
    if cost > edge[node][0]:
        continue
    for a,b in bus[node]:
        if edge[a][0] > cost+b:
            edge[a][0] = cost+b
            edge[a][1] = node
            if a == end:
                continue
            else:
                heapq.heappush(heap, (edge[a][0], a))

result = [end]
while True:
    node = result[-1]
    if node == st:
        break
    result.append(edge[node][1])

print(edge[end][0])
print(len(result))
for i in reversed(result):
    print(i, end=" ")