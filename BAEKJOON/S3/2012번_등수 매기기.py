import sys

# 탐욕법으로 오름차순으로 정렬 후 자기 등수에서 예상 등수를 빼면 가장 적게 나올 것 이다.
def solution(student):
    answer = 0

    for i in range(len(student)):
        current = (i + 1) - student[i]  # (|A - B|)
        if current < 0:
            answer -= current
        else:
            answer += current

    return answer


def main():
    n = int(input())  # 사람 수

    student = sorted([int(sys.stdin.readline().strip()) for _ in range(n)])  # 학생

    print(solution(student))


if __name__=="__main__":
    main()