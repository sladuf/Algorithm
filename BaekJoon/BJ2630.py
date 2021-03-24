# 21.02.04 [색종이 만들기]
import sys

def func(a,b,n):
	if n==1:
		result[p[a][b]] +=1 
		return
	temp = p[a][b]
	for i in range(a,a+n):
		for j in range(b,b+n):
			if p[i][j] != temp:
				func(a,b,n//2)
				func(a,b+n//2,n//2)
				func(a+n//2,b,n//2)
				func(a+n//2,b+n//2,n//2)
				return
	result[temp]+=1

n = int(sys.stdin.readline())
p = []
for i in range(n):
	temp = list(map(int,sys.stdin.readline().split()))
	p.append(temp)

result = [0,0]
func(0,0,n)

print(result[0])
print(result[1])
