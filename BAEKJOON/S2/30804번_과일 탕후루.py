def two_pointer(fru, n):
    left = 0
    fruit_count = [0] * 10  # 과일의 번호가 1~9 이므로 길이 10인 리스트
    max_total = 0
    unique_fruits = 0  # 현재 슬라이딩 윈도우 안에 있는 과일의 종류 개수

    for right in range(n):
        # 현재 과일의 개수를 추가
        if fruit_count[fru[right]] == 0:
            unique_fruits += 1
        fruit_count[fru[right]] += 1

        # 과일 종류가 2개를 초과하면 왼쪽 포인터를 이동
        while unique_fruits > 2:
            fruit_count[fru[left]] -= 1
            if fruit_count[fru[left]] == 0:
                unique_fruits -= 1
            left += 1

        # 두 종류 이하의 과일만 남은 최대 길이를 계산
        max_total = max(max_total, right - left + 1)

    return max_total

# 과일의 개수
n = int(input())

# 과일 리스트
fruit = list(map(int, input().split()))

# 최대 과일 개수 출력
print(two_pointer(fruit, n))
