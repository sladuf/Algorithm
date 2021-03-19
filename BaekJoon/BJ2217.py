# 21.02.03 [로프]
import sys
n = int(sys.stdin.readline())
l = []
for i in range(n):
	l.append(int(sys.stdin.readline()))
l.sort()
result = 0
for i in range(n):
	result = max(l[i]*(n-i), result)
print(result)
