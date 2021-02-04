# 21.02.04 [종이의 개수]
import sys
sys.setrecursionlimit(100000000)

def func(a,b,n):
	global result
	temp = p[a][b]
	for i in range(a,a+n):
		for j in range(b, b+n):
			if temp != p[i][j]:
				for x in range(3):
					for y in range(3):
						func(a+n//3*x, b+n//3*y, n//3)
				return
	result[temp] +=1


n = int(sys.stdin.readline())
p = []
for i in range(n):
	temp = list(map(int, sys.stdin.readline().split()))
	p.append(temp)

result = [0,0,0]

if n == 1:
	result[p[0][0]]+=1
else:
	func(0,0,n)

print(result[-1])
print(result[0])
print(result[1])