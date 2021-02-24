# 21.02.24
'''
동전의 순서를 고려하지 않는것을 주의!!!
하나의 동전을 사용해 만들 수 있는 가짓수를 채워가는 방법
'''
import sys
n,k = map(int,sys.stdin.readline().split())

m=[]
for i in range(n):
	m.append(int(sys.stdin.readline()))
m.sort()

money = [0 for x in range(k+1)]
money[0] = 1

for i in m:
	for j in range(i,k+1):
		money[j] += money[j-i]
print(money[-1])