# 21.03.05 [수 묶기]
'''
양수와 양수가아닌정수(0,음수)를 저장하는 힙 생성
양수에서 a*b < a+b인 경우는 1이 있을 때!!! 그 외에는 무조건 a*b >= a+b
음수에서 a*b < a+b인 경우는 없다. (음*음=양 or 0*음=0) 
'''
import sys
import heapq

n = int(sys.stdin.readline())
plus = []
mius = []
for i in range(n):
	temp = int(sys.stdin.readline())
	if temp > 0:
		#내림차순 힙
		heapq.heappush(plus,-1*temp)
	else:
		#마이너스는 오름차순 힙
		heapq.heappush(mius,temp)

if n == 1:
	if plus:
		print(plus[0])
	else:
		print(mius[0])
else:
	res = 0
	if plus:
		#곱하기가 더 큰 경우 heap에서 pop해서 곱하고
		#1인경우는 더하기가 더 크니까 그만!!!
		#(내림차순 정렬되어있어서 1보다 뒤에 있는 수는 무조건 1)
		num = -1*heapq.heappop(plus)
		while plus:
			temp = -1*heapq.heappop(plus)
			if temp == 1:
				res+=num+temp
				res+=len(plus)
				num=0
				break
			else:
				res+= (num*temp)
				if plus:
					num = -1*heapq.heappop(plus)
				else:
					num=0
					break
		res+=num
	if mius:
		#곱하기가 더 큰 경우 heap에서 pop해서 곱하기 (예외X)
		num = heapq.heappop(mius)
		while mius:
			temp = heapq.heappop(mius)
			res+=(num*temp)
			if mius:
				num=heapq.heappop(mius)
			else:
				num=0
				break
		res+=num
	print(res)