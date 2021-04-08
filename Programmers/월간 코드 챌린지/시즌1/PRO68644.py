from itertools import permutations

def solution(numbers):
    answer = set()
    for a,b in permutations(numbers, 2):
        answer.add(a+b)
    return sorted(list(answer))