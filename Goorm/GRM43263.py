# 21.01.29 [특정 구간의 합]
import sys
n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
a, b = map(int ,sys.stdin.readline().split())

result = 0
for i in range(a-1, b):
	result += l[i]

print(result)