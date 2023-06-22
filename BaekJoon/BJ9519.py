# 2023.06.22
# 졸려

import sys

n = int(sys.stdin.readline())
first = sys.stdin.readline().rstrip()

word = first
words = [first]

for i in range(n):
    st = ""
    end = ""
    for i in range(len(word)):
        if i%2 == 0:
            st += word[i]
        else:
            end += word[i]
    word = st+end[::-1]
    if word == first:
        break
    words.append(word)

print(words[n%len(words)])