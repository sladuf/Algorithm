# 21.02.02 [2048 (Easy)]
'''
괜히 골드2가 아닌것 같아...
조합없이 못살아 정말 못살아
깊은 복사(deepcopy) : 새로운 객체를 만듬 -> 원본 유지하려면 항상 이걸 써야됨!!!
'''

import sys
from itertools import product
from collections import deque
import copy

def check(move):
	global result
	cp = copy.deepcopy(st)
	for now in move:
		if now == 1:
			for i in range(n):
				queue = deque()
				for j in range(n):
					if cp[j][i] == 0:
						continue
					queue.append(cp[j][i])
					cp[j][i] = 0
				if queue:
					temp = queue.popleft()
					cp[0][i] = temp
				cnt = 0
				ch = 0
				while queue:
					temp = queue.popleft()
					if temp == cp[cnt][i]:
						if ch == 0:
							cp[cnt][i] *=2
							ch =1
						else:
							cp[cnt+1][i] = temp
							cnt+=1
							ch = 0
					else:
						cp[cnt+1][i] = temp
						ch = 0
						cnt+=1
		elif now ==2:
			for i in range(n):
				queue = deque()
				for j in range(n-1, -1, -1):
					if cp[j][i] == 0:
						continue
					queue.append(cp[j][i])
					cp[j][i] = 0
				if queue:
					temp = queue.popleft()
					cp[n-1][i] = temp
				cnt = n-1
				ch = 0
				while queue:
					temp = queue.popleft()
					if temp == cp[cnt][i]:
						if ch == 0:
							cp[cnt][i] *=2
							ch =1
						else:
							cp[cnt-1][i] = temp
							cnt-=1
							ch = 0
					else:
						cp[cnt-1][i] = temp
						ch = 0
						cnt-=1
		elif now==3:
			for i in range(n):
				queue = deque()
				for j in range(n):
					if cp[i][j] == 0:
						continue
					queue.append(cp[i][j])
					cp[i][j] = 0
				if queue:
					temp = queue.popleft()
					cp[i][0] = temp
				cnt = 0
				ch = 0
				while queue:
					temp = queue.popleft()
					if temp == cp[i][cnt]:
						if ch == 0:
							cp[i][cnt] *=2
							ch =1
						else:
							cp[i][cnt+1] = temp
							cnt+=1
							ch = 0
					else:
						cp[i][cnt+1] = temp
						ch = 0
						cnt+=1 
		else:
			for i in range(n):
				queue = deque()
				for j in range(n-1, -1, -1):
					if cp[i][j] == 0:
						continue
					queue.append(cp[i][j])
					cp[i][j] = 0
				if queue:
					temp = queue.popleft()
					cp[i][n-1] = temp
				cnt = n-1
				ch=0
				while queue:
					temp = queue.popleft()
					if temp == cp[i][cnt]:
						if ch == 0:
							cp[i][cnt] *=2
							ch =1
						else:
							cp[i][cnt-1] = temp
							cnt-=1
							ch = 0
					else:
						cp[i][cnt-1] = temp
						ch = 0
						cnt-=1
	comp = []
	for i in cp:
		comp.append(max(i))
	comp = max(comp)
	result = max(result, comp)

n = int(sys.stdin.readline())
st = []
for i in range(n):
	temp = list(map(int, sys.stdin.readline().split()))
	st.append(temp)

result = 0
q = [1,2,3,4] #[상,하,좌,우]
for move in product(q, repeat=5):
	check(move)

print(result)
