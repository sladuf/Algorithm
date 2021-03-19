# 21.02.17 [가운데를 말해요]

import sys
import heapq

n = int(sys.stdin.readline())

#정렬을 힙으로 한다는 개념 왼쪽에는 작은 수, 오른쪽엔 큰 수
l = [] #max
r = [] #min
for i in range(n):
	num = int(sys.stdin.readline())
	if len(l) > len(r):
		heapq.heappush(r, (num,num))
	else:
		#l은 max힙이라 -로 우선순위 변경
		heapq.heappush(l, (-num,num))

	if r and l[0][1] > r[0][1]:
		l_pop = heapq.heappop(l)
		r_pop = heapq.heappop(r)
		heapq.heappush(l, (-r_pop[1],r_pop[1]))
		heapq.heappush(r, (l_pop[1],l_pop[1]))

	print(l[0][1])
