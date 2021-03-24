# 21.03.05 [직사각형으로 나누기]
'''
ㅠㅠ 설마 다 돌리는건가 하고 찾아보니 설마가 사람잡은 문제

나눌 수 있는 방법을 다 실행해보고 최대값을 찾는 BP
직사각형 3개로 한정되어 있기 때문에 나눌 수 있는 방법도 한정되어 있다.
=>6가지

나는 범위에 맞으면 반복문을 돌리게 했는데
어차피 범위에 하나라도 안맞으면 abc중에 0이나와서 최대값이랑 비교해도 손색없음
나는 0을 만드는 sum 횟수를 줄이려고 범위를 넣어주었다!
'''
import sys

n,m = map(int, sys.stdin.readline().split())

s=[]
for i in range(n):
	temp=list(map(int,list(sys.stdin.readline().strip())))
	s.append(temp)
res = 0
if n>=3:
	'''
	ㅡ
	ㅡ
	ㅡ
	'''
	for i in range(1,n-1):
		for j in range(i+1,n):
			a=sum([s[x][y] for x in range(i) for y in range(m)])
			b=sum([s[x][y] for x in range(i,j) for y in range(m)])
			c=sum([s[x][y] for x in range(j,n) for y in range(m)])
			res=max(res,a*b*c)
if m>=3:
	'''
	ㅣㅣㅣ
	'''
	for i in range(1,m-1):
		for j in range(i+1,m):
			a=sum([s[x][y] for x in range(n) for y in range(i)])
			b=sum([s[x][y] for x in range(n) for y in range(i,j)])
			c=sum([s[x][y] for x in range(n) for y in range(j,m)])
			res=max(res,a*b*c)

if n>=2 and m>=2:
	'''
	ㅡ
	ㅣㅣ
	'''
	for i in range(1,n):
		for j in range(1,m):
			a=sum([s[x][y] for x in range(i) for y in range(m)])
			b=sum([s[x][y] for x in range(i,n) for y in range(j)])
			c=sum([s[x][y] for x in range(i,n) for y in range(j,m)])
			res=max(res,a*b*c)
	'''
	ㅣㅣ
	ㅡ
	'''
	for i in range(1,n):
		for j in range(1,m):
			a=sum([s[x][y] for x in range(i) for y in range(j)])
			b=sum([s[x][y] for x in range(i) for y in range(j,m)])
			c=sum([s[x][y] for x in range(i,n) for y in range(m)])
			res=max(res,a*b*c)
	'''
	ㅣ=
	'''
	for i in range(1,m):
		for j in range(1,n):
			a=sum([s[x][y] for x in range(n) for y in range(i)])
			b=sum([s[x][y] for x in range(j) for y in range(i,m)])
			c=sum([s[x][y] for x in range(j,n) for y in range(i,m)])
			res=max(res,a*b*c)
	'''
	=ㅣ
	'''
	for i in range(1,m):
		for j in range(1,n):
			a=sum([s[x][y] for x in range(j) for y in range(i)])
			b=sum([s[x][y] for x in range(j,n) for y in range(i)])
			c=sum([s[x][y] for x in range(n) for y in range(i,m)])
			res=max(res,a*b*c)
print(res)
