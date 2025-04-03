def solution(n, s, sequence):
    answer = 1000000000000

    start = 0
    end = 0
    total = 0

    while end < n:
        # total이 s보다 작으면 end를 오른쪽으로 늘림
        total += sequence[end]
        end += 1

        # total이 s 이상일 때 start를 이동시켜서 최소 길이 탐색
        while total >= s:
            answer = min(answer, end - start)
            total -= sequence[start]
            start += 1

    if answer >= 1000000000000:
        return 0
    else:
        return answer


def main():
    # 10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다. 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이 구하기
    n, s = map(int, input().split())

    sequence = list(map(int, input().split()))

    print(solution(n, s, sequence))


main()