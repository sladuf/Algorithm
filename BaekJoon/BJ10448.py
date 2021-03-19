# 21.02.02 [유레카 이론]
def test(num):
	result = 0
	for x in range(1, 45):
		for y in range(1, x+1):
			for z in range(1, y+1):
				if tr[x]+tr[y]+tr[z] == num:
					return 1
				elif tr[x] > num:
					return 0
	return 0

import sys

t = int(sys.stdin.readline())
tr = [0]
temp = 0
for i in range(1, 45):
	temp+=i
	tr.append(temp)

for i in range(t):
	temp = int(sys.stdin.readline())
	print(test(temp))
