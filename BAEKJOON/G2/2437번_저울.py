def solution(weights, len_n):
    # 무게 추를 오름차순으로 정렬
    weights.sort()

    # 만들 수 있는 최대 범위
    max_range = 0

    for weight in weights:
        # 다음 무게 추가 현재 범위 + 1보다 크다면, 그 값은 만들 수 없다.
        if weight > max_range + 1:
            break
        # 범위를 확장
        max_range += weight

    # 만들 수 없는 최소값 반환
    return max_range + 1

if __name__ == "__main__":
    # 몇 개를 입력으로 받을지 개수
    n = int(input())
    # 무게 추
    weight = list(map(int, input().split()))

    print(solution(weight, n))