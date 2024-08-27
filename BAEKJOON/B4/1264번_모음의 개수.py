def solution(s):
    count = 0

    for word in s:
        if word == 'a' or word == 'A' or word == 'e' or word == 'E' or word == 'i' or word == 'I' or word == 'u' or word == 'U' or word == 'o' or word == 'O':
            count += 1

    return count
while True:
    words = input()
    if words == '#':
        break
    else:
        print(solution(words))