# 21.02.15 [회전하는 큐] / Queue
import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
pop = list(map(int, sys.stdin.readline().split()))

q = deque([x for x in range(1, n+1)])

result=0
i=0
while i < m:
	if q[0] == pop[i]:
		q.popleft()
		i+=1
	else:
		temp = q.index(pop[i])
		if temp < len(q)-temp:
			for j in range(temp):
				q.append(q.popleft())
				result+=1
		else:
			for j in range(len(q)-temp):
				q.appendleft(q.pop())
				result+=1
print(result)