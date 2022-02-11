# 22.02.12 [점수 계산]

import sys

score = [[int(sys.stdin.readline()),i] for i in range(8)]

score.sort(key=lambda x: -x[0])

total = 0
quiz = []
for i in range(5):
    total += score[i][0]
    quiz.append(score[i][1])

print(total)
for i in sorted(quiz):
    print(i+1, end=' ')