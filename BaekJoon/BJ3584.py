# 21.03.27 [가장 가까운 공통 조상]
'''
lca 알고리즘 익히기 문제
'''
import sys

t=int(sys.stdin.readline())
for case in range(t):
    n=int(sys.stdin.readline())
    parents=[0 for x in range(n+1)]
    for i in range(n-1):
        a,b=map(int, sys.stdin.readline().split())
		#부모저장
        parents[b]=a

    a,b=map(int, sys.stdin.readline().split())
    a_parents=[a]
    b_parents=[b]
	#a의 조상찾기
    while parents[a]:
        a_parents.append(parents[a])
        a=parents[a]
	#b의 조상찾기
    while parents[b]:
        b_parents.append(parents[b])
        b=parents[b]
    
	#뿌리부터 내려가기 (리스트 제일 끝에 root가 있음)
    a_spot=len(a_parents)-1
    b_spot=len(b_parents)-1
    while a_parents[a_spot]==b_parents[b_spot]:
        a_spot-=1
        b_spot-=1

    print(a_parents[a_spot+1])