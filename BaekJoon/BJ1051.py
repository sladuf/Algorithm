# 21.03.19 [숫자 정사각형]
import sys

n,m=map(int,sys.stdin.readline().split())

s=[]
for i in range(n):
	s.append(list(map(int,list(sys.stdin.readline().strip()))))

l=min(n,m)
res=0
for i in range(n-1):
	for j in range(m-1):
		for k in range(1,l):
			if i+k<n and j+k<m:
				if s[i][j]==s[i][j+k] and s[i][j]==s[i+k][j] and s[i][j]==s[i+k][j+k]:
					res=max(res,k)
			else:
				break
print((res+1)**2)
