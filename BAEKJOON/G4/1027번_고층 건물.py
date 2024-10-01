def bfs(start, count, build):
    # 시작 건물에서 볼 수 있는 건물의 수
    bcount = 0
    # 시작 건물의 높이
    current_high = build[start]

    # 오른쪽 탐색
    current_right_inclination = float('-inf')
    for i in range(start + 1, count):
        high = build[i]
        # 오른쪽의 건물과 기울기 계산
        right_inclination = (high - current_high) / (i - start)

        # 현재 기울기가 이전 기울기보다 가파르거나 첫 번째 건물인 경우
        if right_inclination > current_right_inclination:
            bcount += 1
            current_right_inclination = right_inclination

    # 왼쪽 탐색
    current_left_inclination = float('-inf')
    for i in range(start - 1, -1, -1):
        low = build[i]
        # 왼쪽의 건물과 기울기 계산
        left_inclination = (low - current_high) / (start - i)

        # 현재 기울기가 이전 기울기보다 가파르거나 첫 번째 건물인 경우
        if left_inclination > current_left_inclination:
            bcount += 1
            current_left_inclination = left_inclination

    return bcount

# 건물의 개수
n = int(input())

# 건물의 높이 입력
build = list(map(int, input().split()))

# 각 건물에서 보이는 건물 수를 저장할 리스트
answer = []

# 각 건물에서 bfs 함수를 사용해 보이는 건물 수 계산
for j in range(n):
    answer.append(bfs(j, n, build))

# 그 중에서 가장 많은 건물이 보이는 값을 출력
print(max(answer))