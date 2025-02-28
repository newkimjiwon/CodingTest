def solution(input_string):
    answer = ''

    alpha = {chr(i + 97): 0 for i in range(26)}  # 알파벳

    current = ''  # 현재 상태

    for s in input_string:
        if s != current:  # 다를 경우 갱신
            current = s  # 현재 상태
            alpha[s] += 1  # +1
        else:
            continue  # 전이랑 같으면 돌아감

    # 결과
    for i in alpha:
        if alpha[i] >= 2:  # 2 이상인 알파벳 추가
            answer += i

    if answer == '':
        return 'N'
    else:
        return answer