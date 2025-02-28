answer = 0


def dfs(count, value, ability, visited):
    global answer  # 정답

    student = len(ability)  # 학생
    ex = len(ability[0])  # 종목

    if count == ex:  # 다 선택하면 비교
        answer = max(answer, value)
        return

    for i in range(student):  # 학생 수
        if not visited[i]:
            visited[i] = True  # 현재 학생은 선택
            dfs(count + 1, value + ability[i][count], ability, visited)  # 다른 학생 선택
            visited[i] = False  # 선택했던 학생 풀기


def solution(ability):
    global answer
    answer = 0

    visited = [False] * len(ability)  # 방문

    dfs(0, 0, ability, visited)

    return answer