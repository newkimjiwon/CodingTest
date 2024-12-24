import sys

def count_digits_in_range(start, end):
    """
    주어진 범위(`start`부터 `end`까지)의 숫자에서 각 자리 숫자(0-9)가 몇 번 등장하는지 계산합니다.

    Args:
        start (int): 범위의 시작 숫자.
        end (int): 범위의 끝 숫자.

    Returns:
        list: 각 인덱스에 해당 숫자의 등장 횟수를 담은 리스트.
    """
    counts = [0] * 10
    point = 1

    def add_digits(num, point):
        """숫자 하나의 각 자리수를 계산하여 `counts`에 추가."""
        while num > 0:
            counts[num % 10] += point
            num //= 10

    while start <= end:
        # `end`를 10의 배수 - 1로 조정
        while end % 10 != 9 and end >= start:
            add_digits(end, point)
            end -= 1

        # `start`를 10의 배수로 조정
        while start % 10 != 0 and start <= end:
            add_digits(start, point)
            start += 1

        if start > end:
            break

        # 10의 자리수에 대해 각 숫자의 개수 계산
        start //= 10
        end //= 10
        for i in range(10):
            counts[i] += (end - start + 1) * point

        point *= 10

    return counts

if __name__ == "__main__":
    # 입력 받기
    end = int(sys.stdin.readline().strip())

    # 1부터 `end`까지 각 숫자의 개수 계산
    digit_counts = count_digits_in_range(1, end)

    # 결과 출력
    print(" ".join(map(str, digit_counts)))