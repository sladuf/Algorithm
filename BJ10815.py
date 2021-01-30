# 21.01.30 [숫자 카드]
'''
in으로 탐색하면 1분컷으로 푸는데
시간초과남...
'''
import sys
def merge(num):
	l = 0
	r = n-1
	while l <= r:
		mid = (l+r)//2
		if card[mid] == num:
			return 1
		elif card[mid] > num:
			r = mid-1
		else:
			l = mid+1
	return 0

n = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))

card.sort()
for i in check:
	print(merge(i), end=' ')
