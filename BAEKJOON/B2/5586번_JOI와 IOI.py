def solution(word):
    answer = [0, 0]
    target = ['JOI', 'IOI']

    if len(word) <= 1:
        return answer
    if len(word) <= 2:
        return answer
    if len(word) <= 3:
        if word == target[0]:
            answer[0] += 1
            return answer
        elif word == target[1]:
            answer[1] += 1
            return answer
    
    for i in range(len(word) - 3 + 1):
        parsing = word[i:i+3]
        if parsing == target[0]:
            answer[0] += 1
        elif parsing == target[1]:
            answer[1] += 1

    return answer


if __name__=="__main__":
    word = input()

    answer = solution(word)

    for i in answer:
        print(i)