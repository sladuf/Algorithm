# 21.02.02 [스타트와 링크]
'''
조합에서 -(마이너스)를 이용하면
인덱스 사이의 여집합 조합을 구할 수 있다!!!!!
'''
import sys
from itertools import combinations
n = int(sys.stdin.readline())

s = []
for i in range(n):
	temp = list(map(int, sys.stdin.readline().split()))
	s.append(temp)

member = [x for x in range(n)]
team = []
for i in combinations(member, n//2):
	team.append(i)

result = 100*(n//2)
for i in range(len(team)//2):
	a = team[i]
	b = team[-i-1]
	team1 = 0
	team2 = 0
	for j in range(len(a)-1):
		for k in range(j+1, len(a)):
			team1 += s[a[j]][a[k]] + s[a[k]][a[j]]
			team2 += s[b[j]][b[k]] + s[b[k]][b[j]]
	result = min(result, abs(team1-team2))
	
print(result)
