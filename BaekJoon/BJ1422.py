# 21.02.25 [숫자의 신]
import sys

k,n = map(int, sys.stdin.readline().split())

num = []
for i in range(k):
    temp = sys.stdin.readline().strip()
    num.append(temp)
ad = str(max(map(int,num)))
for i in range(n-k):
    num.append(ad)

#길이가 다른 숫자를 붙여서 큰 수를 만들 때 유용한 정렬부분
#제일 길이가 긴 숫자의 길이만큼, 짧은 숫자들의 길이를 늘여서 비교하여 정렬
num.sort(key = lambda x: x*10, reverse=True)

print(''.join(num))
