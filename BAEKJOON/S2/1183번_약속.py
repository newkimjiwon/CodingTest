def solution(n, wizard):
    # 시간
    times = []

    for a, b in wizard:
        # 시간을 뺀걸 사용
        times.append(a - b)

    # 정렬
    times.sort()

    if len(times) % 2 == 1:
        return 1
    else:
        return abs(times[len(times) // 2] - times[(len(times) // 2) - 1] + 1)


# 메인 함수
def main():
    # n명의 마법사
    n = int(input())

    # 마법사
    wizard = []

    for _ in range(n):
        # 약속 시간 a, 도착 시간 b
        a, b = map(int, input().split())
        wizard.append([a, b])

    print(solution(n, wizard))


if __name__=="__main__":
    main()