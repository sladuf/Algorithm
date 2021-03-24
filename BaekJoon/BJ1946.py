# 21.01.30 [신입 사원]
import sys

t = int(sys.stdin.readline())

for i in range(t):
	n = int(sys.stdin.readline())
	score = []
	for j in range(n):
		a,b = map(int, sys.stdin.readline().split())
		score.append([a,b])
		
	result = 1
	score.sort()
	b = score[0][1]
	for j in range(1, len(score)) :
		if score[j][1] < b:
			b = score[j][1]
			result+=1
	print(result)
