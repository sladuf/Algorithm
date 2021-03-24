# 21.02.07 [가장 큰 수]

def solution(numbers):
    answer = ''
    numbers.sort(key = lambda x: str(x)*3, reverse=True)
    '''
    최대 1000이므로 자릿수를 맞추기 위해 *3
    98 vs 9 -> 989898 vs 999 문자열 비교이므로 8 < 9 라서 9가 98보다 앞으로 정렬됨
    '''
    if numbers[0] == 0:
        return "0"
    for i in numbers:
        answer+=str(i)
    return answer
