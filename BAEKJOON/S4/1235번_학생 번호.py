def solution(s, n):
    answer = 1

    while True:
        # 리스트를 문자열로 변환하여 슬라이싱
        if len({"".join(i[-answer:]) for i in s}) == n:
            break
        answer += 1

    return answer


if __name__ == "__main__":
    # 사람 수 n명
    n = int(input())

    # 학생들
    student = [list(input()) for _ in range(n)]

    print(solution(student, n))