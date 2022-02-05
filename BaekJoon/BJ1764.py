# 22.02.06 [듣보잡]

import sys

n, m = map(int, sys.stdin.readline().split())

no_hear = set()
for i in range(n):
    no_hear.add(sys.stdin.readline().strip())

no_watch = set()
for i in range(m):
    no_watch.add(sys.stdin.readline().strip())

both = sorted(list(no_hear & no_watch))

print(len(both))
print('\n'.join(both))

        
