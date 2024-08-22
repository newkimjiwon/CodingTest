from itertools import combinations

def get_decreasing_number(N):
    decreasing_numbers = []

    # 1자리부터 10자리까지의 모든 줄어드는 수 생성
    for length in range(1, 11):
        for comb in combinations(range(10), length):
            num_str = ''.join(map(str, sorted(comb, reverse=True)))
            decreasing_numbers.append(int(num_str))

    # 모든 줄어드는 수를 정렬
    decreasing_numbers.sort()

    # N번째 줄어드는 수 반환 (N-1 인덱스)
    if N <= len(decreasing_numbers):
        return decreasing_numbers[N - 1]  # N번째 줄어드는 수 (1-based index)
    else:
        return -1  # N번째 줄어드는 수가 존재하지 않는 경우

N = int(input())
result = get_decreasing_number(N)
print(result)