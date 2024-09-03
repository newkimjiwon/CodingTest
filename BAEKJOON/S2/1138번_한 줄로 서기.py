N = int(input())
# 처음 아침에 줄 서는 사람들
people = list(map(int, input().split()))

# 결과 값
result = [0] * N

# 각 위치에 해당하는 인덱스 리스트를 만들어서
# 조건에 맞는 위치를 찾기 위해 사용할 수 있음
available_positions = list(range(N))

# 사람의 번호는 1부터 N까지
for number in range(1, N + 1):
    p = people[number - 1]
    result[available_positions[p]] = number
    available_positions.pop(p)

# 결과 출력
print(" ".join(map(str, result)))