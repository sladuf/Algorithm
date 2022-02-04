# 22.02.05 [단어 뒤집기 2]

import sys

s = sys.stdin.readline().strip()

res = ""
st = []
flag = 0

for i in s:
    if i == '<':
        flag = 1
        if st :
            st.reverse()
            res += "".join(st)
            st = []
        res += i
    elif i == '>':
        flag = 0
        res += i
    elif i == ' ':
        if st:
            st.reverse()
            res += "".join(st)
            st = []
        res += i
    elif flag == 1:
        res += i
    else:
        st.append(i)

if st:
    st.reverse()
    res += "".join(st)
    
print(res)
            