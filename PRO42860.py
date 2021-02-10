# 21.02.08 [조이스틱]
#ㅈㄴ생각하기 어려워 개빡치게
def solution(name):
    answer = 0
    #알파벳 맞추는건 이동과 무관하니까 미리 계산
    for i in range(len(name)):
        temp = ord(name[i])-65
        answer+=min(26-temp,temp)
    name = list(name)
    now = 0
    #이동 계산 이동 후 A로 바꾸고 문자열이 모두 A가 되면 종료
    while True:
        name[now] = 'A'
        if name == ['A']*len(name):
            break
        left = 1
        right = 1
        #오 왼 이동을 이렇게 하면 되는걸...몇시간동안 헤맸네ㅠㅠ
        while name[now-left] == 'A':
            left+=1
        while name[now+right] == 'A':
            right+=1
            
        if right<=left:
            now = now+right
            answer += right
        else:
            now = now-left
            answer += left
        
    return answer
