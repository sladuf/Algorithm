def solution(numbers):
    answer = []
    for num in numbers:
        b_num = bin(num)[2:]
        if '0' in b_num:
            b_num = list(b_num)
            for i in range(len(b_num)-1,-1,-1):
                if b_num[i] == '0':
                    b_num[i] = '1'
                    for j in range(i+1,len(b_num)):
                        if b_num[j] == '1':
                            b_num[j] = '0'
                            break
                    break
            b_num = "".join(b_num)
        else:
            b_num = "0b10" + b_num[1:]
        answer.append(int(b_num,2))
    return answer
