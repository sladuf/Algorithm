# 21.01.31 [수들의 합 2]

import sys

n, m = map(int, sys.stdin.readline().split())

a = list(map(int, sys.stdin.readline().split()))
a.append(0)

result = 0
i = 0
j = 0
now = a[i]
while j < n:
	if now == m:
		result+=1
		now -= a[i]
		i +=1
		j +=1
		now += a[j]
	elif now > m:
		now -= a[i]
		i+=1
		if i > j :
			j = i
			now = a[i]
	else:
		j+=1
		now += a[j]

print(result)
