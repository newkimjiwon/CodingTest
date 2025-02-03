import sys
from collections import Counter


def solution(n, numbers):
    # 정렬하기 (O(N log N))
    numbers.sort()

    # 1. 산술평균 (반올림)
    mean = round(sum(numbers) / n)

    # 2. 중앙값
    median = numbers[n // 2]

    # 3. 최빈값 계산 (O(N))
    count = Counter(numbers)
    max_freq = max(count.values())

    # 최빈값 후보 찾기 (O(N))
    modes = []
    for key, value in count.items():
        if value == max_freq:
            modes.append(key)

    # 정렬 후 두 번째 최빈값 선택
    modes.sort()
    mode = modes[1] if len(modes) > 1 else modes[0]

    # 4. 범위 계산
    num_range = numbers[-1] - numbers[0]

    # 5. 출력
    print(mean)
    print(median)
    print(mode)
    print(num_range)


def main():
    # 입력 최적화
    n = int(sys.stdin.readline().strip())
    numbers = [int(sys.stdin.readline().strip()) for _ in range(n)]

    solution(n, numbers)


if __name__ == "__main__":
    main()