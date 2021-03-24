# 21.02.04 [쿼드트리]

import sys

def func(a,b,c,d):
	if b-a <= 1:
		print(p[a][c], end='')
		return
	temp = p[a][c]
	for i in range(a,b):
		for j in range(c,d):
			if p[i][j] != temp:
				print('(',end='')
				func(a, (a+b)//2, c, (c+d)//2)
				func(a, (a+b)//2, (c+d)//2, d)
				func((a+b)//2, b, c, (c+d)//2)
				func((a+b)//2, b, (c+d)//2, d)
				print(')',end='')
				return
	print(temp,end='')

n = int(sys.stdin.readline())

p = []
for i in range(n):
	temp = list(sys.stdin.readline().strip())
	temp = list(map(int, temp))
	p.append(temp)

func(0,n,0,n)
