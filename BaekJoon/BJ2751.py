# 21.01.30 [수 정렬하기2]

import sys

n = int(sys.stdin.readline())

st = []
for i in range(n):
	st.append(int(sys.stdin.readline()))
for i in sorted(st):
	print(i)
