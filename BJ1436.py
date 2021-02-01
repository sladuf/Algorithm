# 21.02.01 [영화감독 숌]

import sys
n = int(sys.stdin.readline())

now=1
result = 666
while n > now:
	result+=1
	if '666' in str(result):
		now+=1
print(result)