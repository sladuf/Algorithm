# 22.02.09 [신입 사원]

import sys

t = int(sys.stdin.readline())

for i in range(t):
	n = int(sys.stdin.readline())
	arr = []
	for j in range(n):
		a,b = map(int, sys.stdin.readline().split())
		arr.append([a,b])
	arr.sort()
	res = 1
	mx = arr[0][1]
	for i in range(n):
		if mx > arr[i][1]:
			res+=1
			mx = arr[i][1]
	print(res)
