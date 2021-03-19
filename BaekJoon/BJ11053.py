# 21.01.29 [가장 긴 증가하는 부분 수열]
import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

result = [1 for i in range(n)]

for i in range(1, n):
	for j in range(i):
		if a[i] > a[j] and result[i] < result[j]+1:
			result[i] = result[j]+1
print(max(result))

