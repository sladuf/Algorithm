# 21.02.09 [전화번호 목록]
import sys

t = int(sys.stdin.readline())

for i in range(t):
	n = int(sys.stdin.readline())
	arr = []
	for j in range(n):
		temp = sys.stdin.readline().strip()
		arr.append(temp)
	arr.sort()
	flag = True
	for j in range(1, n):
		if arr[j].startswith(arr[j-1]):
			print("NO")
			flag = False
			break
	if flag : print("YES")