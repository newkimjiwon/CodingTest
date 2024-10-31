# 입력 처리
n, m = map(int, input().split())
six_set = 1001  # 패키지 가격의 초기값 (최대값보다 큰 값으로 설정)
each = 1001     # 낱개 가격의 초기값 (최대값보다 큰 값으로 설정)

# 각 브랜드의 패키지 및 낱개 가격을 입력받으며 최소값 갱신
for _ in range(m):
    s, e = map(int, input().split())
    six_set = min(six_set, s)
    each = min(each, e)

# 최소 비용 계산
# 1. 전부 패키지로만 구매하는 경우
cost_all_sets = ((n // 6) + 1) * six_set

# 2. 전부 낱개로만 구매하는 경우
cost_all_each = n * each

# 3. 패키지와 낱개를 조합하는 경우
cost_mixed = (n // 6) * six_set + (n % 6) * each

# 최소 비용 출력
result = min(cost_all_sets, cost_all_each, cost_mixed)
print(result)