# 21.02.05 [소트인사이드]

import sys
l = list(sys.stdin.readline().strip())
l = list(map(int, l))
for i in sorted(l,reverse=True):
	print(i,end='')
