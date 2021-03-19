# 21.02.24 [2xn 타일링 2]
import sys

n = int(sys.stdin.readline())
if n == 1:
	print(1)
elif n == 2:
	print(3)
else:
	res = 0
	a = 1
	b = 3
	for i in range(3, n+1)
		c = a*2 + b
		res = c
		a = b
		b = c
	print(res%10007)