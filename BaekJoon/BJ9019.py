# 21.03.06 [DSLR]
'''
완탐은 내스타일 아닌것 같다..
알고리즘은..BFS..?

조건을 잘 보자!!!
n=0이면 9999가 저장되는데 n-1=0이면 으로 잘못 읽어서 개고생함 ㅜㅜ; 
'''
import sys
from collections import deque


t=int(sys.stdin.readline())

for case in range(t):
    a,b = map(int, sys.stdin.readline().split())
    visited=[False for x in range(10000)]
    q=deque([[a,""]])
    while q:
        n,m=q.popleft()
        temp=(n*2)%10000
        if temp==b:
            print(m+'D')
            break
        elif not visited[temp]:
            visited[temp]=True
            q.append([temp,m+'D'])

        #n=0이면 9999를 대신 저장
        if n==0:
            temp=9999
        else:
            temp=n-1
        if temp==b:
            print(m+'S')
            break
        elif not visited[temp]:
            visited[temp]=True
            q.append([temp,m+'S'])

        '''
        뼈를 깎은 부분 ㅠㅠ
        temp=네자리의 str을 만들어준다.(50이면 0050으로 바꿔줌)
        '''
        temp='0'*(4-len(str(n)))+str(n)
        l=int(temp[1:]+temp[0])
        r=int(temp[3]+temp[:3])
        if l==b:
            print(m+'L')
            break
        elif r==b:
            print(m+'R')
            break
        if not visited[l]:
            visited[l]=True
            q.append([l,m+'L'])
        if not visited[r]:
            visited[r]=True
            q.append([r,m+'R'])

'''
다른 사람이 푼 L,R 부분
수학을 잘 하는게 답인건가...?

        temp=int(n%1000*10+n/1000)
        if temp==b:
            print(m+'L')
            break
        elif not visited[temp]:
            visited[temp]=True
            q.append([temp,m+'L'])

        temp=int(n%10*1000+n//10)
        if temp==b:
            print(m+'R')
            break
        elif not visited[temp]:
            visited[temp]=True
            q.append([temp,m+'R'])
'''
