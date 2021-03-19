# 21.01.30 [시리얼 번호]
'''
lambda 로 sorting할 key갑 지정가능!!! 개유용해!!!!!
'''
import sys

n= int(sys.stdin.readline())
serial = []
result = []
for i in range(n):
	temp = sys.stdin.readline().strip()
	length = len(temp)
	num = 0
	for j in temp:
		if j.isdigit(): num+=int(j)
	serial.append([temp, length, num])

serial.sort(key = lambda x: (x[1], x[2], x[0]))
for i in serial:
	print(i[0])