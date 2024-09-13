n, m = map(int, input().split())

line = list(map(int, input().split()))
line.sort()

result = []
used = [False] * n  # 각 숫자가 사용되었는지를 추적하기 위한 리스트

def dfs():
    if len(result) == m:
        print(' '.join(map(str, result)))
        return

    prev = -1  # 이전에 사용한 숫자를 저장
    for i in range(n):
        if not used[i] and prev != line[i]:  # i번째 숫자가 사용되지 않았으면
            used[i] = True  # 현재 숫자를 사용한 것으로 표시
            result.append(line[i])
            dfs()
            prev = line[i]
            result.pop()
            used[i] = False  # 숫자를 사용하지 않은 상태로 돌려놓음

dfs()