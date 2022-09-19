# https://school.programmers.co.kr/learn/courses/30/lessons/17677

'''
<조건>
1. 각 문자열의 길이는 2 이상, 1,000 이하이다.
2. 입력으로 들어온 문자열은 두 글자씩 끊어서 다중집합의 원소로 만든다.
3. 이때 영문자로 된 글자 쌍만 유효하고, 기타 공백이나 숫자, 특수 문자가 들어있는 경우는 그 글자 쌍을 버린다.
4. 대문자와 소문자의 차이는 무시한다.
5. 유사도 값은 0에서 1 사이의 실수이므로, 이를 다루기 쉽도록 65536을 곱한 후에 소수점 아래를 버리고 정수부만 출력한다.
'''

def divideStr(string):
    result = []
    for i in range(0, len(string)):
        tmp = string[i:i+2]
        if tmp.isalpha() and len(tmp) == 2:
            print(tmp)
            result.append(tmp)

    return result

def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    divideStr1 = divideStr(str1)
    divideStr2 = divideStr(str2)
    a = set(divideStr1) & set(divideStr2) #교집합
    b = set(divideStr1) | set(divideStr2) #합집합

    allA = float(sum([min(divideStr1.count(i), divideStr2.count(i)) for i in a]))
    allB = float(sum([max(divideStr1.count(i), divideStr2.count(i)) for i in b]))

    answer = int((1 if (allA==0 and allB==0) else (allA/allB)) * 65536)

    return answer

str1 = "FRANCE"
str2 = "french"
result = solution(str1, str2)
print(result)