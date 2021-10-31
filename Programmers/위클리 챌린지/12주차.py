from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    # 순열을 이용하여 brute force
    for i in permutations(dungeons, len(dungeons)):
        temp = 0
        temp_k = k
        for j in i:
            if j[0] <= temp_k:
                temp_k -= j[1]
                temp+=1
        answer=max(answer, temp)
        
    return answer
