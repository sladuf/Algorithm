def solution(files):
    answer = []
    sorting = []
    for i in range(len(files)):
        head = ""
        index = 0
        for j in range(len(files[i])):
            if files[i][j].isdigit():
                index = j
                break
            head += files[i][j]
        number = ""
        for j in range(j, len(files[i])):
            if not files[i][j].isdigit():
                break
            number += files[i][j]
        sorting.append([head.upper(), int(number), i])
        
    sorting.sort(key = lambda x: (x[0], x[1], x[2]))
    
    for f in sorting:
        answer.append(files[f[2]])
    
    return answer
