def main():
    answer = 0
    n = int(input())
    sequence = []

    # 입력 수열 생성
    for _ in range(n):
        num = int(input())
        sequence.append(num)

    # 1은 따로 세기 (곱하는 것보다 더하는 게 이득)
    ones = sequence.count(1)
    sequence = [x for x in sequence if x != 1]

    # 0 존재 여부 확인 (음수 단독 제거 용도)
    zero_count = sequence.count(0)
    sequence = [x for x in sequence if x != 0]

    # 양수, 음수 나누기
    positives = [x for x in sequence if x > 1]
    negatives = [x for x in sequence if x < 0]

    positives.sort(reverse=True)
    negatives.sort()

    # 양수: 큰 수부터 곱
    for i in range(0, len(positives), 2):
        if i + 1 < len(positives):
            answer += positives[i] * positives[i + 1]
        else:
            answer += positives[i]

    # 음수: 작은 수부터 곱
    for i in range(0, len(negatives), 2):
        if i + 1 < len(negatives):
            answer += negatives[i] * negatives[i + 1]
        else:
            if zero_count == 0:
                answer += negatives[i]
            # else: 0과 곱해서 무시됨

    # 1은 무조건 더함
    answer += ones

    print(answer)


if __name__ == "__main__":
    main()