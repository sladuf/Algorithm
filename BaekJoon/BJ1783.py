# 21.02.03 [병든 나이트]
import sys

n,m = map(int, sys.stdin.readline().split())

if n == 1:
	print(1)
elif n == 2:
	if m < 3:
		print(1)
	elif m < 5:
		print(2)
	elif m < 7:
		print(3)
	else:
		print(4)
else:
	if m < 4:
		print(m)
	elif m < 7:
		print(4)
	else:
		print(m-2)
