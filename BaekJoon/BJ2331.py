# 21.03.04 [반복수열]
import sys

a,b = map(int,sys.stdin.readline().split())

res = [a]

while True:
	num = 0
	for i in str(res[-1]):
		num+=int(i)**b
	if num in res:
		t = res.index(num)
		res = res[:t]
		break
	else:
		res.append(num)

print(len(res))
