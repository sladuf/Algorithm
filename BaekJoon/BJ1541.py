# 21.02.03 [잃어버린 괄호]

import sys
from collections import deque

ex = list(sys.stdin.readline().strip())

make = []
total = []
minus = False
for i in range(len(ex)):
	if ex[i].isdigit():
		make.append(ex[i])
	else:
		total.append(int(''.join(make)))
		make = []
		if ex[i] == '-':
			total.append(ex[i])
			minus = True
		elif minus:
			total.append('-')
			make.append(ex[i])
		else:
			total.append(ex[i])
total.append(int(''.join(make)))

result = total[0]
for i in range(2, len(total), 2):
	if total[i-1] == '+':
		result += total[i]
	else:
		result -= total[i]
print(result)
