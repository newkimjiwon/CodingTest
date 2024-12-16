def main():
    # 정수 n를 입력
    n = int(input())

    words = [input() for _ in range(n)]

    result = []

    for word in words:
        len_word = len(word)
        s = ''
        if len_word == 1:
            s += word[0]
            s += word[0]
            result.append(s)
        else:
            s += word[0]
            s += word[-1]
            result.append(s)

    for r in result:
        print(r)

main()