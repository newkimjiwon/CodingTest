def iterative_dfs(start, graph, visited, finished, team):
    stack = [start]
    path = []
    while stack:
        student = stack.pop()
        if not visited[student]:
            visited[student] = True
            path.append(student)
            next_student = graph[student]
            if not visited[next_student]:
                stack.append(next_student)
            elif not finished[next_student]:  # 사이클 발견
                # 팀에 속한 학생들 세기
                while next_student != student:
                    team.add(next_student)
                    next_student = graph[next_student]
                team.add(student)
                break
        else:
            path.pop()
    
    for student in path:
        finished[student] = True

T = int(input())
answer = []

for _ in range(T):
    student = int(input())
    graph = [0] + list(map(int, input().split()))
    
    visited = [False] * (student + 1)
    finished = [False] * (student + 1)
    team = set()
    
    for i in range(1, student + 1):
        if not visited[i]:
            iterative_dfs(i, graph, visited, finished, team)
    
    # 팀에 속하지 않는 학생 수 계산
    answer.append(student - len(team))

for i in answer:
    print(i)