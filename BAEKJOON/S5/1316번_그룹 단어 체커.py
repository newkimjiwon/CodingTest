def solution(s):
    stack = []

    alpha = {chr(i + 96) : 0 for i in range(1, 27)}

    for word in s:
        if not stack:
            stack.append(word)
            continue
        if stack[-1] == word:
            continue
        elif stack[-1] != word:
            stack.append(word)
    
    for st in stack:
        alpha[st] += 1
        if alpha[st] == 2:
            return False
    
    return True

# 단어의 개수
N = int(input())

# 단어 모아둔 곳
words = []

# 카운트
count = 0

for _ in range(N):
    word = list(input())
    if solution(word):
        count += 1

print(count)