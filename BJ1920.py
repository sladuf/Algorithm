# 21.02.17 [수 찾기]
import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
a.sort()

for i in range(m):
	l = 0
	r = len(a)-1
	flag = False
	while l<=r:
		mid = (l+r)//2
		if a[mid] == num[i]:
			print(1)
			flag=True
			break
		if a[mid] > num[i]:
			r = mid-1
		else:
			l = mid+1
	if flag == False:
		print(0)