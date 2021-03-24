# 21.02.14 [단속카메라]

def solution(routes):
    routes.sort()
    now=routes[-1][0]
    answer=1
    for i in range(len(routes)-2,-1,-1):
        if routes[i][1] < now:
            now=routes[i][0]
            answer+=1
            
    return answer
