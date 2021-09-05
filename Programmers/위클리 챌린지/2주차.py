def solution(scores):
    answer = ''
    
    for i in range(len(scores)):
        l = False
        s = False
        my = scores[i][i]
        total = my
        for j in range(len(scores)):
            if i==j:
                continue
            if my == scores[j][i]:
                l = True
                s = True
            elif my < scores[j][i]:
                l = True
            else:
                s = True
            total+=scores[j][i]
        
        if l and s:
            total = total/len(scores)
        else:
            total = (total-my)/(len(scores)-1)
        
        if total>=90:
            answer+='A'
        elif total>=80:
            answer+='B'
        elif total>=70:
            answer+='C'
        elif total>=50:
            answer+='D'
        else:
            answer+='F'
            
    return answer
