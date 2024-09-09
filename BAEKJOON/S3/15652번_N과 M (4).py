# N은 숫자가 나올 수 있는 최대, M은 수열의 길이
N, M = map(int, input().split())

answer = []

def dfs(start):
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return

    for i in range(start, N + 1):
        answer.append(i)
        dfs(i)
        answer.pop()

dfs(1)