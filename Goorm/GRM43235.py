# 21.02.01 [징검다리]
import sys
from itertools import combinations
d, n, m = map(int, sys.stdin.readline().split())
nm = n-m
l = []
for i in range(n):
	l.append(int(sys.stdin.readline()))
l.sort()
result=[]
for i in combinations(l, nm):
	temp = i[0]
	for j in range(1, nm):
		temp = min(temp, i[j]-i[j-1])
	temp = min(temp, d-i[-1])
	result.append(temp)
print(max(result))
