# 21.02.25 [책 나눠주기]
import sys

t = int(sys.stdin.readline())
for i in range(t):
	n,m = map(int, sys.stdin.readline().split())
	book = [True for x in range(n+1)]
	st = []
	for j in range(m):
		a,b = map(int, sys.stdin.readline().split())
		st.append([a,b])
	st.sort(key = lambda x: (x[1],x[0]))
	res = 0
	
	for a,b in st:
		for x in range(a,b+1):
			if book[x]:
				book[x] = False
				res+=1
				break
	print(res)
