
def solution(lan, k):
    lan.sort(reverse = True)  # 내림차순으로 바꾸기
    left = 1  # 1부터
    right = lan[0]  # 가장 긴 길이부터 시작
    answer = 0  # 결과 값

    while left <= right:
        cut = (left + right) // 2
        current = sum(i // cut for i in lan)

        if current >= k:
            answer = cut  # 가능하므로 정답 후보로 저장
            left = cut + 1  # 더 큰 길이도 시도
        else:
            right = cut - 1  # 너무 많이 잘라서 개수가 모자람

    return answer


def main():
    n, k = map(int, input().split())

    lan = [int(input()) for _ in range(n)]

    print(solution(lan, k))


main()