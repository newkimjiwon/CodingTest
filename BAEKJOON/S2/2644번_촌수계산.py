from collections import deque


def solution(graph, n, start, end):
    dq = deque([(start, 0)])

    # 한 번 방문했던 친척은 재방문하지 않는다.
    visited = [False] * (n + 1)
    visited[start] = True

    while dq:
        relative, count = dq.popleft()

        if relative == end:
            return count

        # 다른 친척을 찾는다.
        for i in graph[relative]:
            if not visited[i]:
                dq.append((i, count + 1))
                visited[i] = True

    # 결과가 없다면 -1를 출력
    return -1


def main():
    n = int(input())  # 전체사람의 수

    a, b = map(int, input().split())  # 촌수를 계산해야하는 사람

    m = int(input())  # 부모 자식의 관계 수

    graph = {i: [] for i in range(1, n + 1)}

    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    print(solution(graph, n, a, b))


if __name__=="__main__":
    main()