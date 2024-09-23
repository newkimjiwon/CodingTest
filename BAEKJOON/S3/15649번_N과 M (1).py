def dfs():
    if len(answer) == m:
        print(' '.join(answer))
        return
    for i in range(n):
        if not visited[i]:
            answer.append(per[i])
            visited[i] = True
            dfs()
            answer.pop()
            visited[i] = False

n, m = map(int, input().split())

per = []
# 재방문을 막기 위한 배열
visited = [False] * n
# 결과 값을 출력하는 배열
answer = []

for i in range(1, n + 1):
    per.append(str(i))

dfs()