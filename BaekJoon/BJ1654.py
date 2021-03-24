# 21.02.17 [랜선 자르기]

import sys

n,m = map(int, sys.stdin.readline().split())
li =[int(sys.stdin.readline()) for x in range(n)]

l = 1
r = max(li)*2
result = 0
while l<=r:
	mid = (l+r)//2
	k = 0
	for i in li:
		k += i//mid
	if k >= m:
		l = mid+1
		result = mid
	else:
		r = mid-1
print(result)
