# https://school.programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = ''
    pad = {}
    k=1
    for i in range(4):
        for j in range(3):
            pad[k] = [i,j]
            k+=1
    print(pad)
    
    l = 10
    r = 12
    for i in numbers:
        if i in [1,4,7]:
            answer+='L'
            l=i
        elif i in [3,6,9]:
            answer+='R'
            r=i
        else:
            if i==0:
                i=11
                
            la, lb = pad[l]
            ra, rb = pad[r]
            ia, ib = pad[i]
            ll = abs(la-ia)+abs(lb-ib)
            rr = abs(ra-ia)+abs(rb-ib)
            if ll==rr:
                if hand == 'right':
                    answer+='R'
                    r=i
                else:
                    answer+='L'
                    l=i
            elif ll<rr:
                answer+='L'
                l=i
            else:
                answer+='R'
                r=i
                
    return answer