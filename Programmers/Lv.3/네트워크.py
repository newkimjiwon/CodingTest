def DFS(x, visited, computers, n):
    visited[x] = True

    for i in range(n):
        if not visited[i] and computers[x][i] == 1:
            DFS(i, visited, computers, n)


def solution(n, computers):
    answer = 0

    visit = [False] * n

    for i in range(n):
        if not visit[i]:
            DFS(i, visit, computers, n)
            answer += 1

    return answer