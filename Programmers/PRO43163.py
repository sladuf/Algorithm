# 21.02.09 [단어 변환]

from collections import deque

def solution(begin, target, words):
    if not(target in words):
        return 0
    queue = deque()
    queue.append([begin,0])
    while queue:
        word, num = queue.popleft()
        if word == target:
            return num
        for i in range(len(words)):
            temp = 0
            #방문한적 없는 words만 검사함
            if words[i] != 0 :
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        temp+=1
                #다른 글자가 한글자면 queue에 넣는다
                #방문의 의미로 words[i]를 0으로 바꿈
                if temp <= 1:
                    queue.append([words[i],num+1])
                    words[i] = 0
    return 0
