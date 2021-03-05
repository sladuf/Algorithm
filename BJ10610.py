# 21.03.05 [30]
'''
@@ 30의 배수는 맨 뒷자리가 0이고 나머지 자릿수의 합이 3의 배수이다.
'''
import sys
from itertools import permutations

n = list(sys.stdin.readline().strip())

if '0' not in n:
	print(-1)
else:
	s = sum(map(lambda x: int(x),n))
	if s % 3 == 0:
		print(''.join(sorted(n,reverse = True)))
	else:
		print(-1)