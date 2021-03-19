# 21.02.03 [동전 0]
import sys
n,k = map(int, sys.stdin.readline().split())
a = []
for i in range(n):
	a.append(int(sys.stdin.readline()))

result = 0
for i in range(n-1, -1, -1):
	temp = 0
	if a[i] <= k:
		temp = k//a[i]
		result += temp
		k -= temp*a[i]
print(result)
