# 21.02.13 [파도반 수열]
import sys

p = [1 for x in range(100)]
p[0] = 1
p[1] = 1 
p[2] = 1

for i in range(3, 100):
    p[i] = p[i-2]+p[i-3]

n = int(sys.stdin.readline())

for i in range(n):
    temp = int(sys.stdin.readline())
    print(p[temp-1])
