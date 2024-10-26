def find_lexicographically_smallest(word):
    min_word = None

    # 모든 가능한 i, j 위치에 대해 나누기
    for i in range(1, len(word) - 1):
        for j in range(i + 1, len(word)):
            # 세 부분으로 나누기
            part1 = word[:i]
            part2 = word[i:j]
            part3 = word[j:]

            # 각각 뒤집어서 새로운 단어 만들기
            new_word = part1[::-1] + part2[::-1] + part3[::-1]

            # 최소 사전순 단어 업데이트
            if min_word is None or new_word < min_word:
                min_word = new_word

    return min_word

word = input()
print(find_lexicographically_smallest(word))