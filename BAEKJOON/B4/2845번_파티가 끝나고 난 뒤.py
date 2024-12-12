# 입력 처리
L, P = map(int, input().split())
articles = list(map(int, input().split()))

# 계산
actual_count = L * P
differences = [article - actual_count for article in articles]

# 출력
print(" ".join(map(str, differences)))