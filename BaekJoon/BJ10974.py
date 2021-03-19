# 21.02.02 [모든 순열]

import sys
from itertools import permutations

n = int(sys.stdin.readline())
comb = [x for x in range(1, n+1)]

for i in permutations(comb, n):
	for j in i:
		print(j, end=' ')
	print()