# 21.01.30 [접미사 배열]
import sys
from collections import deque

s = sys.stdin.readline().strip()
dic = []

for i in range(len(s)):
	dic.append(s[i:])

for i in sorted(dic):
	print(i)