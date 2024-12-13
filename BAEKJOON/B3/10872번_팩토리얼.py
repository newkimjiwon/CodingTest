def main():
    # 정수 n를 입력
    n = int(input())

    if n == 0:
        print(1)
    else:
        answer = 1
        for i in range(1, n + 1):
            answer *= i
        print(answer)

main()