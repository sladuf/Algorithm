# 22.02.16 [정수 삼각형]
import sys

n=int(sys.stdin.readline())

tree = []
for i in range(n):
	temp = list(map(int, sys.stdin.readline().split()))
	tree.append(temp)
	if i == 0:
		continue
	tree[i][0] += tree[i-1][0]
	tree[i][-1] += tree[i-1][-1]
	for j in range(1,i):
		tree[i][j] += max([tree[i-1][j-1], tree[i-1][j]])

print(max(tree[-1]))