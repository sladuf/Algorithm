# 21.02.11 [전화번호 목록]
def solution(phone_book):

    phone_book.sort(key=lambda x:(x, len(x)))
    for i in range(0,len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if phone_book[j].startswith(phone_book[i]):
                return False
    return True