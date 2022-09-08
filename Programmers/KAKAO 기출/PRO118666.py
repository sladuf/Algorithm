# https://school.programmers.co.kr/learn/courses/30/lessons/118666?language=python3

def point(a,b,p):
    if p == 1:
        return [a,3]
    elif p == 2:
        return [a,2]
    elif p == 3:
        return [a,1]
    elif p == 4:
        return [False]
    elif p == 5:
        return [b,1]
    elif p == 6:
        return [b,2]
    elif p == 7:
        return [b,3]

def test(result):
    returnData = ""

    data = [["R","T"],["C","F"],["J","M"],["A","N"]]
    for d in data:
        first = d[0]
        sec = d[1]
        if first in result and sec in result:
            returnData += first if result[first] >= result[sec] else sec
        elif first in result or sec in result:
            returnData += first if first in result else sec
        else:
            returnData += first

    return returnData
            


def solution(survey, choices):
    answer = ''
    result = dict()
    for ab,p in zip(survey,choices):
        a = ab[0]
        b = ab[1]
        res = point(a, b, p)
        if res[0]:
            t = res[0]
            p = res[1]
            if t in result :
                result[t] += p
            else:
                result[t] = p
    
    answer = test(result)

    return answer


survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
print(solution(survey, choices))