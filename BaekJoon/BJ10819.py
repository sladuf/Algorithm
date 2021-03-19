# 21.02.02 [차이를 최대로]

import sys
from itertools import permutations

n = int(sys.stdin.readline())
l = list(map(int,sys.stdin.readline().split()))
result = -100*n
for i in permutations(l, n):
	temp = 0
	for j in range(1, n):
		temp += abs(i[j-1]-i[j])
	result = max(result, temp)
print(result)

