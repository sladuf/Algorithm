# 21.02.05 [통계학]
import sys
from collections import defaultdict

n = int(sys.stdin.readline())

num = []
total = 0
for i in range(n):
	temp = int(sys.stdin.readline())
	num.append(temp)
	total += temp
num.sort()

print(round(total/n)) #산술평균
print(num[n//2]) #중앙

dic = defaultdict(int)
max_count  = 0
temp = 0
ptr = 0
for i in num:
	dic[i] +=1
for i in dic:
	if dic[i] > max_count:
		max_count = dic[i]
		ptr = i
		temp = 1
	elif dic[i] == max_count and temp == 1:
		ptr = i
		temp = 0

print(ptr) #최빈
print(num[-1]-num[0]) #범위
