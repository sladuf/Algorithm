# 22.02.16 [GRB거리]

'''
위 값의 최소 + 내꺼
'''

import sys

n=int(sys.stdin.readline())

rgb = [[0,0,0]]
for i in range(1, n+1):
	r,g,b = map(int, sys.stdin.readline().split())
	rgb.append([r,g,b])
	rgb[i][0] += min([rgb[i-1][1],rgb[i-1][2]])
	rgb[i][1] += min([rgb[i-1][0],rgb[i-1][2]])
	rgb[i][2] += min([rgb[i-1][0],rgb[i-1][1]])

print(min(rgb[n]))