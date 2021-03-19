# 21.02.01 [토너먼트]
'''
구글링 해서 풀었는데 브루트포스도 규칙찾기인가...
-1이 나오는 경우가 없는데 문제에 주어지는 건...ㅠ
'''
import sys
from collections import deque

n,a,b =map(int, sys.stdin.readline().split())

result=0
while a!=b:
	a -= a//2
	b -= b//2
	result+=1
print(result)
