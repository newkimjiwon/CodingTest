N = int(input())

# 리스트
NGE = list(map(int, input().split()))

# 결과를 저장할 리스트, 초기값은 -1로 설정
result = [-1] * N

# 스택, 저장할 값은 (NGE[i], i)
stack = []

# 역순으로 탐색
for i in range(N - 1, -1, -1):
    # 스택에서 현재 NGE[i]보다 작은 값들을 제거
    while stack and stack[-1] <= NGE[i]:
        stack.pop()

    # 스택이 비어있지 않다면, 오큰수를 결과에 기록
    if stack:
        result[i] = stack[-1]

    # 현재 값을 스택에 추가
    stack.append(NGE[i])

# 결과 출력
print(' '.join(map(str, result)))