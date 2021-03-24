# 21.02.05 [구명보트]

def solution(people, limit):
    answer = 0
    people.sort()
    a = 0
    b = len(people)-1
    #n안에 끝나니까 나름 효율..?
    while a<=b:
        if a==b:
            answer+=1
            break
        #보트에 탈 수 있는 사람이 두명이면 a+=1
        if people[a] + people[b] <= limit:
            a+=1
        b-=1
        #어차피 두명이나 한명이나 한배에 태우면 +=1
        answer+=1
        
    return answer
