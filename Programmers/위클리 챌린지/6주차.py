def solution(weights, head2head):
    w = []
    
    for i in range(len(weights)):
        temp = [0,0,weights[i],-(i+1)]
        cnt = 0
        for j in range(len(weights)):
            if head2head[i][j] == 'N':
                continue
            if head2head[i][j] == 'W':
                temp[0]+=1
                if weights[i] < weights[j]:
                    temp[1]+=1
            cnt+=1
            
                    
        if temp[0]:
            temp[0] = temp[0]/cnt
        
        w.append(temp)
        
    w.sort(reverse=True)
    
    answer = []
    for i in w:
        answer.append(-i[3])
    
    return answer
