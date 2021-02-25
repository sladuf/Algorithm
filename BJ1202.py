# 21.02.25 [보석 도둑]
'''
보석과 가방을 무게 순서대로 정렬
보석의 무게가 가방보다 가볍거나 같은거 다 heap정렬(가격기준으로 내림차순)
정렬이 끝나면 그 중에 젤 가격 높은거 pop
다음 가방 무게랑 비교해서 가방 갯수만큼 계속 반복
'''
import sys
import heapq

n,k = map(int, sys.stdin.readline().split())
gold = []
bag = []
for i in range(n):
	a,b = map(int, sys.stdin.readline().split())
	heapq.heappush(gold,[a,b])
for i in range(k):
	a = int(sys.stdin.readline())
	bag.append(a)

bag.sort()

# w는 가격 기준으로 내림차순 하는 heap
w = []
res = 0
for i in bag:
	while gold:
		if gold[0][0] <= i:
			a,b = heapq.heappop(gold)
			heapq.heappush(w,-b)
		else:
			break
	if w:
		res+= -1*heapq.heappop(w)
print(res)
