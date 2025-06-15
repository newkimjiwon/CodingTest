def reverse_words(S):
    result = []         # 최종 결과 리스트
    word = []           # 현재 단어 저장용
    in_tag = False      # 태그 안에 있는지 여부

    for char in S:
        if char == '<':
            # 단어가 있다면 먼저 뒤집어서 결과에 추가
            if word:
                result.extend(reversed(word))
                word.clear()
            in_tag = True
            result.append(char)

        elif char == '>':
            in_tag = False
            result.append(char)

        elif in_tag:
            # 태그 안에서는 그대로 추가
            result.append(char)

        elif char == ' ':
            # 공백을 만나면 단어를 뒤집고 공백 추가
            if word:
                result.extend(reversed(word))
                word.clear()
            result.append(' ')

        else:
            # 단어 구성 문자라면 word에 추가
            word.append(char)

    # 마지막에 단어가 남아 있으면 뒤집어서 추가
    if word:
        result.extend(reversed(word))

    print(''.join(result))


# 입력 및 실행
S = input().strip()
reverse_words(S)