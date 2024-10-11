# 입력받기
n, m = map(int, input().split())
lst = [input().strip() for _ in range(n)]
k = int(input())

max_cnt = 0

# 모든 행에 대해 반복
for row in range(n):
    # 현재 행의 0의 개수 세기
    zero_count = lst[row].count('0')

    # 이 행과 똑같은 값을 가진 행의 개수 세기
    col_light_cnt = 0

    # 0의 개수와 k의 짝수/홀수 조건을 확인
    if zero_count <= k and (k - zero_count) % 2 == 0:
        for other_row in range(n):
            if lst[row] == lst[other_row]:  # 두 개의 행이 같으면
                col_light_cnt += 1  # 1을 더해준다

    max_cnt = max(max_cnt, col_light_cnt)  # 최대값보다 크면 업데이트

print(max_cnt)