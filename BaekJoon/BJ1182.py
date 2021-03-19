# 21.02.01 [부분수열의 합]
import sys
from itertools import combinations
n,s = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

result=0
for i in range(1, n+1):
	for j in combinations(a, i):
		if sum(j) == s:
			result+=1
			
print(result)
