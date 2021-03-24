# 21.03.05 [날짜 계산]

import sys

e,s,m = map(int, sys.stdin.readline().split())
a,b,c, = 1,1,1
res = 1
while True:
	if a==e and b==s and c==m:
		print(res)
		break
	else:
		a+=1
		b+=1
		c+=1
		res+=1
		if a > 15:
			a=1
		if b > 28:
			b=1
		if c > 19:
			c=1
