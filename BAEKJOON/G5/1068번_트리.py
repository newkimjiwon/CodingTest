def make_graph(nodes, len_n, delete):
    # 노드를 이용해서 그래프로 변환한다.
    graph = [[] for _ in range(len_n)]
    # 방문한 곳은 다시 방문하지 않도록 처리
    visit = [False] * len_n

    # 삭제될 노드는 방문하지 않는다.
    visit[delete] = True

    # 시작 노드를 결정
    root = -1

    # answer 전역 변수
    global answer

    for i in range(len_n):
        if nodes[i] == -1:
            root = i
            # 삭제 노드가 부모노드이면 0을 반환한다.
            if delete == root:
                return 0
        else:
            # 삭제된 노드와 연결된 노드 추가하지 않음
            if i != delete and nodes[i] != delete:
                graph[nodes[i]].append(i)

    dfs(graph, root, visit, delete)

    return answer

def dfs(graphs, start, visited, delete):
    visited[start] = True

    # 현재 노드의 모든 자식 노드를 탐색
    child_count = 0
    for child in graphs[start]:
        if not visited[child] and child != delete:
            dfs(graphs, child, visited, delete)
            child_count += 1

    # 자식 노드가 없으면 리프 노드로 간주
    if child_count == 0:
        global answer
        answer += 1

if __name__ == "__main__":
    # 노드의 개수
    n = int(input())

    # 노드
    node = list(map(int, input().split()))

    # 삭제될 노드
    d = int(input())

    answer = 0

    print(make_graph(node, n, d))