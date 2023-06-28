# 2023.06.28

def solution(today, terms, privacies):
    answer = []
    today = dateToDay(today)
    
    dic = dict()
    for i in terms:
        t,n = i.split(" ")
        dic[t] = int(n)*28
    
    for i in range(len(privacies)):
        time,term = privacies[i].split(" ")
        temp = dateToDay(time) + dic[term]
        if today >= temp:
            answer.append(i+1)
    
    return answer


def dateToDay(time):
    y,m,d = map(int, time.split("."))
    return (y*12*28)+(m*28)+d