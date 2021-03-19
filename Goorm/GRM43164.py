# 21.02.01 [점심은 햄버거]
import sys

n = int(sys.stdin.readline())
eat = list(map(int, sys.stdin.readline().split()))
hot = list(map(int, sys.stdin.readline().split()))
h = []
for i in range(n):
	h.append([eat[i],hot[i]])
h.sort(reverse = True)

result = 0
temp = 0
for i in range(n):
	temp += h[i][1]
	result = temp+h[i][0]
print(result)