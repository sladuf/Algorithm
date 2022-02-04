# 22.01.31 [스택]
import sys

n = int(sys.stdin.readline())

st = []

for i in range(n):
    temp = sys.stdin.readline().split()
    if temp[0] == "push":
        st.append(int(temp[1]))
    elif temp[0] == "pop":
        if st :
            ptr = st.pop()
            print(ptr)
        else:
            print(-1)
    elif temp[0] == "size":
        print(len(st))
    elif temp[0] == "empty":
        if st:
            print(0)
        else:
            print(1)
    else:
        if st:
            print(st[-1])
        else:
            print(-1)

