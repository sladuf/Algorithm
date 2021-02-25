# 21.02.25 [예산]

import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
a.sort()
l = m//len(a)
r = a[-1]
res = 0
while l<=r:
	mid = (l+r)//2
	total = 0
	for i in a:
		if i>=mid:
			total+=mid
		else:
			total+=i
		if total > m:
			break

	if total>m:
		r = mid-1
	else:
		l = mid+1
		res = mid
print(res)