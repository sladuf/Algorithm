# 21.01.29 [길찾기(다이아몬드)]
import sys
n = int(sys.stdin.readline())
dia = []
for i in range(2*n-1):
	temp = list(map(int, sys.stdin.readline().split()))
	dia.append(temp)

for i in range(1, n):
	for j in range(len(dia[i])):
		if j == 0:
			dia[i][0] += dia[i-1][0]
		elif j == len(dia[i])-1 :
			dia[i][j] += dia[i-1][j-1]
		else:
			dia[i][j] += max(dia[i-1][j-1], dia[i-1][j])

for i in range(n, 2*n -1):
	for j in range(len(dia[i])):
		dia[i][j] += max(dia[i-1][j], dia[i-1][j+1])

print(dia[2*n-2][0])