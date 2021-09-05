def solution(s):
    
    st = []
    for temp in s:
        if st and st[-1] == temp:
            st.pop()
        else:
            st.append(temp)
            
            
    if st:
        return 0
    else:
        return 1
