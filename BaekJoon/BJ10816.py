# 21.02.17 [숫자 카드 2]
import sys
from collections import defaultdict

n = int(sys.stdin.readline())
dic = defaultdict(int)

for i in list(map(int, sys.stdin.readline().split())):
    dic[i] += 1

m = int(sys.stdin.readline())
for i in list(map(int, sys.stdin.readline().split())):
    print(dic[i])
    
