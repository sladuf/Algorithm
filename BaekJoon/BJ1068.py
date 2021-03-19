# 21.02.02 [트리]

import sys
from collections import defaultdict

def dfs(now):
	global result
	if not dic[now]:
		result+=1
		return
	for i in dic[now]:
		dfs(i)

n = int(sys.stdin.readline())
node = list(map(int, sys.stdin.readline().split()))
delete = int(sys.stdin.readline())
dic = defaultdict(list)
for i in range(n):
	if i == delete or node[i] == delete:
		continue
	dic[node[i]].append(i)

result=0
if dic[-1]:
	dfs(-1)
print(result)