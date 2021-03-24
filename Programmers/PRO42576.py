# 21.02.11 [완주하지 못한 선수]

def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    j = 0
    for i in completion:
        if i != participant[j]:
            break
        j+=1
    answer = participant[j]
        
    return answer
