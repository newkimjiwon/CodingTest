# 사람의 수 N과 파티의 수 M
n, m = map(int, input().split())

# 결과값
answer = 0

# 진실을 아는 사람 초기화
knows = set(map(int, input().split()[1:]))

# 파티 정보 저장
party = []
for _ in range(m):
    party.append(set(map(int, input().split()[1:])))

# 진실을 아는 사람 집합 확장
for _ in range(m):  # 최대 M번 반복
    for p in party:
        if knows & p:  # 교집합이 존재하면 진실을 아는 사람들과 연결됨
            knows.update(p)  # 진실을 아는 사람 집합에 추가

# 거짓말이 가능한 파티 개수 계산
for p in party:
    if not (knows & p):  # 교집합이 없으면 진실을 아는 사람이 없음
        answer += 1

print(answer)