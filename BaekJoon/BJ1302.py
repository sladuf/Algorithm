# 22.02.12 [베스트셀러]

import sys
from collections import Counter

n = int(sys.stdin.readline())

books = []
for i in range(n):
    books.append(sys.stdin.readline().strip())

res = Counter(books).most_common()
res.sort(key=lambda x:(-x[1],x[0]))
print(res[0][0])