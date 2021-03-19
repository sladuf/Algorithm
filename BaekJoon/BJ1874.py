# 21.02.15 [스택 수열]
import sys

n = int(sys.stdin.readline())

s = []
for j in range(n):
	s.append(int(sys.stdin.readline()))

result = ['+']
stack = [1]
i = 0
num = 2
while num <= n :
	if not stack or stack[-1] != s[i]:
		stack.append(num)
		result.append('+')
		num+=1
		continue

	stack.pop()
	result.append('-')
	i+=1

while stack:
	if stack[-1] == s[i]:
		result.append('-')
		i+=1
		stack.pop()
	else:
		print('NO')
		break

if len(stack) == 0:
	for i in result:
		print(i)
