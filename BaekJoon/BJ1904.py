# 21.02.13 [01타일]
import sys

n = int(sys.stdin.readline())

a = 1
b = 2
c = n

for i in range(2, n):
    c = (a+b)%15746
    a = b
    b = c

print(c%15746)
