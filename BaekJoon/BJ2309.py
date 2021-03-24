# 21.02.01 [일곱 난쟁이]

import sys
from itertools import combinations

height = []
for i in range(9):
	height.append(int(sys.stdin.readline()))

result = []
for i in combinations(height, 7):
	if sum(i) == 100:
		result = i
		break

		
for i in sorted(result):
	print(i)
