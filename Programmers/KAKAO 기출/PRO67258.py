# 2023.06.27
# 보석 쇼핑
from collections import defaultdict

def solution(gems):
    answer = [0,len(gems)]
    
    n = len(set(gems))
    my = set()
    dic = defaultdict(int)
    
    l = 0
    r = 0
    while r < len(gems):
        dic[gems[r]]+=1
        my.add(gems[r])
        while n == len(my):
            dic[gems[l]]-=1
            if dic[gems[l]] == 0:
                my.remove(gems[l])
            if answer[1]-answer[0] > r-l:
                answer = [l+1,r+1]
            l+=1
        r+=1
            
    return answer

# set으로 진열대에 있는 보석 종류 찾기
# 딕셔너리에 보석 저장하면서 새로운 set에 보석 추가
# 기존 set의 길이와 새로운 set의 길이가 같아질 때까지 추가
# 같아졌으면? -> 길이를 줄여가며 확인
