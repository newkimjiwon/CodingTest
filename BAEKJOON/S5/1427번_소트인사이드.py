if __name__ == "__main__":
    # 숫자를 입력
    word = input()

    # str를 int 리스트로 변경
    num = list(map(int, str(word)))

    # 내림차순으로 변경
    num.sort(reverse = True)

    # 결과 값을 출력하는 for문
    for i in num:
        print(i, end = '')