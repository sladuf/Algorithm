# 21.01.30 [전화번호 목록]
import sys

t = int(sys.stdin.readline())

for i in range(t):
	n = int(sys.stdin.readline())
	call = []
	for j in range(n):
		call.append(sys.stdin.readline().strip())
	call.sort()
	flag = False
	for j in range(1, n):
		if call[j].startswith(call[j-1]):
			print("NO")
			flag = True
			break
	if flag == False:
		print("YES")
