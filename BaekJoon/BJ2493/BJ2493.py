# 22.02.06 [탑]
import sys

n = int(sys.stdin.readline())
top = list(map(int, sys.stdin.readline().split()))


st = []
res = [0] * n

def search(num):
    value = top[num]
    while st:
        if value <= st[-1][1]:
            res[num] = st[-1][0] +1
            break
        else:
            st.pop()

for i in range(n):
    search(i)
    st.append([i,top[i]])

for i in res:
    print(i, end = ' ')