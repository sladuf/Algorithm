# 21.02.09 [여행경로]
from collections import defaultdict

def solution(tickets):
	#pop()할때 오름차순으로 꺼내려면 reverse 해줘야됨
    tickets.sort(reverse=True)
    dic = defaultdict(list)
    for a,b in tickets:
        dic[a].append(b)
    
    stack = ['ICN']
    answer = []
    while stack:
        temp = stack[-1]
        #'temp가 출발지가 아니면' 이라는 뜻
        if len(dic[temp]) == 0:
            answer.append(temp)
            stack.pop()
        else:
            stack.append(dic[temp].pop())

    #stack에서 나오는건 뒤에꺼 부터니까 reverse해주기
    answer.reverse()
    return answer
