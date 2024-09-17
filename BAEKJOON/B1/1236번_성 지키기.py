# 입력 받기
N, M = map(int, input().split())
castle = [input().strip() for _ in range(N)]

# 경비원이 없는 행과 열을 체크하기 위한 변수
rows_without_guard = 0
cols_without_guard = 0

# 각 행에 경비원이 있는지 확인
for i in range(N):
    if 'X' not in castle[i]:
        rows_without_guard += 1

# 각 열에 경비원이 있는지 확인
for j in range(M):
    if 'X' not in [castle[i][j] for i in range(N)]:
        cols_without_guard += 1

# 행과 열 중 더 큰 값을 출력
print(max(rows_without_guard, cols_without_guard))