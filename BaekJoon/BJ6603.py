# 21.02.04 [로또]
import sys
from itertools import combinations

while True:
	temp = list(map(int, sys.stdin.readline().split()))
	if temp[0] == 0:
		break
		
	for lotto in combinations(temp[1:], 6):
		for num in lotto:
			print(num, end=' ')
		print()
	print()
