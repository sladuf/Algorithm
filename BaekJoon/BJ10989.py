# 21.02.05 [수 정렬하기3]
import sys
n = int(sys.stdin.readline())
num = [0]*10001
for i in range(n):
	temp = int(sys.stdin.readline())
	num[temp]+=1
for i in range(1, 10001):
	if num[i] != 0:
		for j in range(num[i]):
			print(i)
