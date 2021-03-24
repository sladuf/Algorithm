# 21.02.14 [섬 연결하기]

def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    #방문 node 체크 하는 집합
    node = set([costs[0][0]])
    
    while len(node)<n:
        for a,b,c in costs:
            if a in node and b in node :
                continue
            elif a in node or b in nogiotde:
                node.update([a,b])
                answer += c
                break
        
    return answer
