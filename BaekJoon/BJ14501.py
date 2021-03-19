# 21.02.01 [퇴사]

import sys
n = int(sys.stdin.readline())
s=[]
for i in range(n):
	t, p = map(int, sys.stdin.readline().split())
	s.append([t,p])

result = [0 for i in range(n)]

for i in range(n-1, -1, -1):
	j = i + s[i][0]
	if j < n :
		result[i] += max(result[j:]) + s[i][1]
	if j == n:
		result[i] = s[i][1]
print(max(result))
