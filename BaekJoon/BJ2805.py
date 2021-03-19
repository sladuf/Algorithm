# 21.02.17 [나무 자르기]
import sys

n,m = map(int, sys.stdin.readline().split())
namu = list(map(int, sys.stdin.readline().split()))

l = 0
r = max(namu)
result = 0
while l<=r:
	mid = (l+r)//2
	h=0
	for i in namu:
		if i <= mid:
			continue
		h+=(i-mid)

	if h < m:
		r = mid-1
	else:
		l = mid+1
		result = mid

print(result)
