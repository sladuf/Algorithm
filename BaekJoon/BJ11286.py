# 21.02.17 [절댓값 힙]
import sys
import heapq

n = int(sys.stdin.readline())
h =[]
for i in range(n):
	x = int(sys.stdin.readline())
	if x == 0:
		if h:
			#값이 튜플로 나옴 두번째가 찐 number
			print(heapq.heappop(h)[1])
		else:
			print(0)
	else:
		heapq.heappush(h,(abs(x),x))
		
