from collections import defaultdict

def solution(record):
    dic = defaultdict(str)
    
    answer = []
    for temp in record:
        temp = temp.split()
        if temp[0][0] == 'E':
            dic[temp[1]]=temp[2]
            answer.append([temp[0],temp[1]])
        elif temp[0][0] == 'L':
            answer.append([temp[0],temp[1]])
        else:
            dic[temp[1]]=temp[2]
    
    for i in range(0, len(answer)):
        if answer[i][0] == 'Enter':
            answer[i] = '{}님이 들어왔습니다.'.format(dic[answer[i][1]])
        else:
            answer[i] = '{}님이 나갔습니다.'.format(dic[answer[i][1]])
    
    return answer
