# 21.02.03 [단어 수학]
'''
존나 천재 블로거의 도움을 받음
수학적 띵킹.....
'''
import sys
from collections import defaultdict

n=int(sys.stdin.readline())
words=[]
for i in range(n):
	words.append(list(sys.stdin.readline().strip()))
dic = defaultdict(int)

for word in words:
	length = len(word)-1
	for i in word:
		dic[i] += 10**length
		length-=1

num =9
result = 0
for i in sorted(dic.items(), key=lambda x: x[1], reverse = True):
	result += num *i[1]
	num-=1
print(result)