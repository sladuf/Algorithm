# 22.02.06 [회사에 있는 사람]

import sys

n = int(sys.stdin.readline())

dic = dict()
name = set()

for i in range(n):
    temp = sys.stdin.readline().split()
    if temp[1] == 'enter':
        name.add(temp[0])
    dic[temp[0]] = temp[1]

for i in sorted(name, reverse=True):
    if dic[i] == 'enter':
        print(i)

