# 21.02.11 [베스트앨범]
from collections import defaultdict

def solution(genres, plays):
    answer = []
    total = defaultdict(int)
    dic = defaultdict(list)
    for i in range(len(genres)):
        total[genres[i]]+=plays[i]
        dic[genres[i]].append([i,plays[i]])

    total = sorted(total.items(), key=lambda x:x[1],reverse=True)
    for i in dic:
        dic[i].sort(key=lambda x :(x[1],-x[0]))

    for a,b in total:
        for i in range(2):
            if dic[a]:
                temp = dic[a].pop()
                answer.append(temp[0])
                
    return answer