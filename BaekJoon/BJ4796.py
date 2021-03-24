# 21.02.03 [캠핑]
import sys

case = 0
while True:
	case+=1
	l,p,v = map(int, sys.stdin.readline().split())
	if l == 0:
		break
	result = 0
	while v > 0:
		if v-p >= 0 or v > l:
			result +=l
			v -= p
		else:
			result +=v
			v-=v
			
	print("Case "+str(case)+": "+str(result))
