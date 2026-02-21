import sys

# 방향 W와 크기 N 입력
w, n = sys.stdin.readline().split()
n = int(n)

# 배열 입력
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 숫자 변환 규칙 함수
def transform(num):
    if num == 1: return '1'
    if num == 2: return '5'
    if num == 5: return '2'
    if num == 8: return '8'
    return '?'

# 결과 배열 생성
result = [['' for _ in range(n)] for _ in range(n)]

for r in range(n):
    for c in range(n):
        # 상하 뒤집기 (U, D)
        if w in ('U', 'D'):
            target_r = n - 1 - r
            target_c = c
        # 좌우 뒤집기 (L, R)
        else:
            target_r = r
            target_c = n - 1 - c
            
        result[target_r][target_c] = transform(matrix[r][c])

# 출력
for row in result:
    print(*(row))