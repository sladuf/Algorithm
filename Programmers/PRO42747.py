# 21.02.07 [H-Index]

def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    h=0
    #i가 문제의 h의 역할을, h는 h번 이상 인용된 논문의 갯수임
    for i in range(len(citations),-1,-1):
        #h는 논문의 갯수보다 클 수 없음
        while h < len(citations):
            if citations[h] >= i:
                h+=1
            else:
                break
        if h>=i:
            answer = i
            return answer
