# 입력 받기
word = input()

# 문자 개수
answer = 0
# 반복문 사용
i = 0

while i < len(word): 
    if word[i] == 'c':
        if i + 1 < len(word) and (word[i + 1] == '=' or word[i + 1] == '-'):
            i += 2
            answer += 1
            continue
    elif word[i] == 'd':
        if i + 2 < len(word) and word[i + 1] == 'z' and word[i + 2] == '=':
            i += 3
            answer += 1
            continue
        elif i + 1 < len(word) and word[i + 1] == '-':
            i += 2
            answer += 1
            continue
    elif word[i] == 'l' or word[i] == 'n':
        if i + 1 < len(word) and word[i + 1] == 'j':
            i += 2
            answer += 1
            continue
    elif word[i] == 's' or word[i] == 'z':
        if i + 1 < len(word) and word[i + 1] == '=':
            i += 2
            answer += 1
            continue
    answer += 1
    i += 1

print(answer)