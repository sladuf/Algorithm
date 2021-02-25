# 21.02.25 [카드 정렬하기]
import sys
import heapq

n = int(sys.stdin.readline())
h = []
for i in range(n):
	temp = int(sys.stdin.readline())
	heapq.heappush(h,temp)
res = 0
while len(h) > 1:
	a = heapq.heappop(h)
	b = heapq.heappop(h)
	res += a+b
	heapq.heappush(h,a+b)

print(res)