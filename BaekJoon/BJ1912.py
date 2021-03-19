# 21.01.29 [연속합]

import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

result = a[:]
for i in range(1, n):
	if result[i-1] >= a[i-1]:
		result[i] = max(a[i], result[i-1] + a[i])
	elif result[i-1] < a[i-1]:
		result[i] = max(a[i], a[i] + a[i-1])

print(max(result))