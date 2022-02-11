# 22.02.12 [보석 도둑]

import sys, heapq

n,k = map(int, sys.stdin.readline().split())

bosuk = []
for i in range(n):
	a,b = map(int, sys.stdin.readline().split())
	heapq.heappush(bosuk,[a,b])

bag = []
for i in range(k):
	bag.append(int(sys.stdin.readline()))

bag.sort()

res = 0
temp = []
for weight in bag:
	while bosuk:
		if weight >= bosuk[0][0]:
			a,b = heapq.heappop(bosuk)
			heapq.heappush(temp, -b)
		else:
			break
	if temp:
		res += heapq.heappop(temp)
print(-1*res)
