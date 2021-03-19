# 21.02.08 [큰 수 만들기]
def solution(number, k):
    answer = ''
    stack = []
    kk = 0
    #앞에서부터 작은거 제거
    #(높은 자릿수의 수가 클수록 ㄱㅇㄷ이니까)
    for i in range(len(number)):
        while stack:
            temp = stack[-1]
            if temp < number[i]:
                stack.pop()
                kk+=1
            else: break
            if kk==k:
                break
        stack.append(number[i])
        
        #k만큼 제거 했으면 남은 수 stack에 넣기
        if kk==k:
            for j in range(i+1, len(number)):
                stack.append(number[j])
            break

    #앞에서 작은거 제거 했는데 k가 남으면 뒤에서부터 제거     
    if kk<k:
        for i in range(k-kk):
            stack.pop()
    answer = "".join(stack)

    return answer
