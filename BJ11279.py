# 21.02.17 [최대 힙]
import sys
import heapq

n = int(sys.stdin.readline())
h = []

for i in range(n):
	temp = int(sys.stdin.readline())
	if temp == 0:
		if h:
			print(heapq.heappop(h)*-1)
		else:
			print(0)
	else:
		heapq.heappush(h,temp*-1)