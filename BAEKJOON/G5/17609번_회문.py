def solution(words):
    left = 0
    right = len(words) - 1

    # 1단계: 문자열 양 끝에서 출발하는 포인터로 순수 회문 여부를 먼저 검사한다.
    while left < right:
        if words[left] == words[right]:
            # 양쪽 문자가 같으면 검사 범위를 한 칸씩 줄이며 안쪽으로 이동한다.
            left += 1
            right -= 1
        else:
            # 최초 불일치 지점을 찾으면 그 위치를 기준으로 유사회문 검사를 시도한다.
            break

    # 포인터가 서로 교차하거나 같은 인덱스에서 멈췄다면 이미 완전한 회문이다.
    if left >= right:
        return 0

    # 2단계: 왼쪽 문자가 문제였다고 가정하고 해당 문자를 건너뛴 상태로 다시 비교한다.
    left_1 = left + 1
    right_1 = right
    while left_1 < right_1:
        if words[left_1] == words[right_1]:
            left_1 += 1
            right_1 -= 1
        else:
            # 한 글자를 건너뛴 뒤에도 불일치가 발생하면 이 가정은 실패.
            break

    if left_1 >= right_1:
        return 1

    # 3단계: 이번에는 오른쪽 문자를 제거했다고 가정하고 동일한 검사를 반복한다.
    left_2 = left
    right_2 = right - 1
    while left_2 < right_2:
        if words[left_2] == words[right_2]:
            left_2 += 1
            right_2 -= 1
        else:
            # 오른쪽 제거 가정도 성립하지 않으면 더 이상 시도할 방법이 없다.
            break

    if left_2 >= right_2:
        return 1

    # 어떤 문자 하나를 제거해도 회문이 되지 않는 일반 문자열이다.
    return 2


if __name__ == "__main__":
    T = int(input())

    # 입력으로 주어진 T개의 문자열 각각에 대해 결과를 출력한다.
    for _ in range(T):
        words = input()
        print(solution(words))
