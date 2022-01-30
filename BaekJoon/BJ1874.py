# 22.01.31 [스택 수열]
import sys
from collections import deque

n = int(sys.stdin.readline())
arr = deque()

for i in range(n):
    arr.append(int(sys.stdin.readline()))

res = []

st = []
num = 1
while num <= n :
    if st and st[-1] == arr[0]: 
        if st[-1] == arr[0]:
            arr.popleft()
            st.pop()
            res.append("-")
    else:
        st.append(num)
        res.append("+")
        num+=1


for i in range(len(arr)):
    if st[-1] == arr[0]:
        arr.popleft()
        st.pop()
        res.append("-")
    else:
        break

if st :
    print("NO")
else:
    for i in res:
        print(i)