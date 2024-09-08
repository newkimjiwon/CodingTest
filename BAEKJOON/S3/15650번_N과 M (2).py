from itertools import permutations

# N은 숫자가 나올 수 있는 최대, M은 수열의 길이
N, M = map(int, input().split())

# 결과
answer = []

result = []

for i in range(1, N + 1):
    result.append(i)

for i in permutations(result, M):
    current = list(i)
    current.sort()

    if current not in answer:
        answer.append(current)

for i in answer:
    print(' '.join(map(str, i)))