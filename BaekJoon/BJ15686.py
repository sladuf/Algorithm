# 21.02.02 [치킨 배달]

def length(num):
	total = 0
	for x in range(n):
		for y in range(n):
			if info[x][y] == 1:
				short = n*n
				for z in num:
					short = min(short, abs(x-z[0])+abs(y-z[1]))
				total+=short
	return total

import sys
from itertools import combinations

n,m = map(int, sys.stdin.readline().split())

info = []
for i in range(n):
	temp = list(map(int, sys.stdin.readline().split()))
	info.append(temp)

ch = []
for i in range(n):
	for j in range(n):
		if info[i][j] == 2:
			ch.append([i,j])
			

result = []
for i in combinations(ch, m):
	result.append(length(i))

print(min(result))
