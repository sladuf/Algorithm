# 21.02.15 [덱]
import sys
from collections import deque

n = int(sys.stdin.readline())

dq = deque()
for i in range(n):
	temp = sys.stdin.readline().strip().split()
	if temp[0] == 'push_front':
		dq.appendleft(temp[1])
	elif temp[0] == 'push_back':
		dq.append(temp[1])
	elif temp[0] == 'pop_front':
		if dq:
			print(dq.popleft())
		else:
			print(-1)
	elif temp[0] == 'pop_back':
		if dq:
			print(dq.pop())
		else:
			print(-1)
	elif temp[0] == 'size':
		print(len(dq))
	elif temp[0] == 'empty':
		if dq:
			print(0)
		else:
			print(1)
	elif temp[0] == 'front':
		if dq:
			print(dq[0])
		else:
			print(-1)
	else:
		if dq:
			print(dq[-1])
		else:
			print(-1)
