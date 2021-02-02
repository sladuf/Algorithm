# 21.02.02 [리모컨]
import sys

def check(ch):
	temp = True
	for i in ch:
		if i in bt:
			temp = False
			break
	return temp

n = list(sys.stdin.readline().strip())
m = int(sys.stdin.readline())
bt = []
if m > 0 :
	bt = list(sys.stdin.readline().strip().split())
num = int(''.join(n))

if m == 10 :
	print(abs(100-num))
else:
	if check(str(num)) or num==100:
		print(min(abs(num-100),len(n)))
	else:
		l = num-1
		r = num+1
		while True:
			if l >= 0 and check(str(l)):
				print(min(len(str(l))+abs(num-l),abs(100-num)))
				break
			elif check(str(r)):
				print(min(len(str(r))+abs(num-r),abs(100-num)))
				break
			l-=1
			r+=1