# 21.02.01 [체스판 다시 칠하기]

import sys
n,m = map(int,sys.stdin.readline().split())
bw = []
for i in range(n):
	temp = list(sys.stdin.readline().strip())
	bw.append(temp)

result=8*8
for i in range(7, n):
	for j in range(7, m):
		temp1 = 0
		temp2 = 0
		for a in range(i-7, i+1):
			for b in range(j-7, j+1):
				if (a+b) %2 ==0:
					if bw[a][b] == 'B':
						temp2+=1
					else:
						temp1+=1
				else:
					if bw[a][b] == 'W':
						temp2+=1
					else:
						temp1+=1
		result =min(temp1, temp2, result)
print(result)
