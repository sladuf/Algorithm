# 21.02.23 [텀 프로젝트]
import sys
from collections import deque

def ch(i):
	global res

	q = deque([i])
	num = st[i]
	st[i] = False

	while q:
		if st[num]:
			q.append(num)
			temp = num
			num = st[temp]
			st[temp] = False
		else:
			#방문하고자 하는 수가 이미 방문했다면? ( == False)
			#방문하고자 하는 수가 s1이라면 현재 q에 있는 수들은 팀이 된다.
			if q[0] == num:
				res += len(q)
				break
			else:
				q.popleft()


t = int(sys.stdin.readline())
for i in range(t):
	n = int(sys.stdin.readline())
	st = [0] + list(map(int,sys.stdin.readline().split()))
	res = 0
	for i in range(len(st)):
		if st[i] :
			ch(i)

	print(n-res)
