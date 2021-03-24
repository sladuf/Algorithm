# 21.02.19 [최단경로]
import sys
import heapq
from collections import defaultdict
from math import inf

v,e = map(int, sys.stdin.readline().split())

st = int(sys.stdin.readline())
dic = defaultdict(list)
for i in range(e):
	a,b,c = map(int, sys.stdin.readline().split())
	dic[a].append([c,b])

visited = [inf for x in range(v+1)]

q = []
heapq.heappush(q,(0,st))
while q:
	a,b = heapq.heappop(q)
	for x in dic[b]:
		if visited[x[1]] > x[0]+a:
			visited[x[1]] = x[0]+a
			heapq.heappush(q,(x[0]+a,x[1]))

for i in range(1,v+1):
	if i == st :
		print(0)
	elif visited[i] == inf:
		print('INF')
	else:
		print(visited[i])
