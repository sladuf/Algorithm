# 21.01.31 [수리공 항승]
import sys

n, l = map(int, sys.stdin.readline().split())
spot = list(map(int, sys.stdin.readline().split()))

spot.sort()

now = spot.pop()
result =1
while spot:
	temp = spot.pop()
	if now-temp >= l:
		now = temp
		result+=1
		
print(result)
