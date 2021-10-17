def solution(sizes):
    answer = [0,0]
    for temp in sizes:
        x = max(temp)
        y = min(temp)
        
        if answer[0] < x:
            answer[0] = x
        if answer[1] < y:
            answer[1] = y
        
    return answer[0]*answer[1]
