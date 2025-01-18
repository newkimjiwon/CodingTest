def solution(s):
    answer = 0

    # 현재 스코어
    score = 0

    for i in s:
        if i == 'O':
            score += 1
            answer += score
        else:
            score = 0
    
    return answer


if __name__=="__main__":
    n = int(input())

    # 결과 값을 담은 배열
    result = []

    for _ in range(n):
        # OX 퀴즈
        question = input()
        result.append(solution(question))

    for i in result:
        print(i)