from collections import deque

def solution(s):
    answer = 0
    q=deque(s)
    for i in range(len(s)):
        stack=[]
        flag=True
        for j in q:
            if j=='[' or j=='(' or j=='{':
                stack.append(j)
            elif not stack:
                flag=False
                break
            elif j==']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    flag=False
                    break
            elif j==')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    flag=False
                    break
            elif j=='}':
                if stack[-1] == '{':
                    stack.pop()
                else:
                    flag=False
                    break
        if not stack and flag:
            answer+=1
        q.append(q.popleft())
            
    return answer