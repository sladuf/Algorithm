# https://school.programmers.co.kr/learn/courses/30/lessons/60059

'''
1. key를 오른쪽으로 회전하는 함수 (총 4번)
2. 회전한 키로 brute force -> lock을 *3 해서 index error 나지 않게 하기
3. 일치하는지 검사하는 함수

회전 rule
x = y
y = len(n)-1-x
'''

def rotation(key):
    lenk = len(key)
    result = [[0]*lenk for _ in range(lenk)]
    for x in range(0, lenk):
        for y in range(0, lenk):
            result[y][lenk-1-x] = key[x][y]
    print(result)
    return result

def check(lock3):
    n = len(lock3)//3
    for i in range(n):
        for j in range(n):
            if lock3[n+i][n+j] >= 2 or lock3[n+i][n+j] == 0:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    # lock을 3배로 키워주기
    lock3 = [[0]*(n*3) for _ in range(n*3)]
    # 가운데에 lock 넣기
    for i in range(n):
        for j in range(n):
            lock3[n+i][n+j] = lock[i][j]
    
    for i in range(4):
        key = rotation(key)
        for x in range(n*2):
            for y in range(n*2):
                for keyX in range(len(key)):
                    for keyY in range(len(key)):
                        lock3[x+keyX][y+keyY] += key[keyX][keyY]
                if check(lock3):
                    return True
                else:
                    for keyX in range(len(key)):
                        for keyY in range(len(key)):
                            lock3[x+keyX][y+keyY] -= key[keyX][keyY]

    return False

# TEST
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
result = solution(key, lock)
print(result)