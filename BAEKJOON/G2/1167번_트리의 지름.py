from collections import deque


def solution(v, graph):
    answer = 0

    # 1번째 BFS 임의의 점에서 시작하면 되니깐 0에서 시작해도 된다.
    # 임의의 점에서 가장 먼 노드를 찾아야한다.
    q = deque([(1, 0)])
    visited = [False] * (v + 1)  # 방문 처리
    visited[1] = True
    distance = [0] * (v + 1)  # 비용

    while q:
        node, weight = q.popleft()

        for next_node, next_wegiht in graph[node]:
            total_weight = weight + next_wegiht   # 가중치 총합

            if not visited[next_node]:
                distance[next_node] = max(total_weight, distance[next_node])  # 새로운 가중치 값이 더 크면 새롭게 갱신
                visited[next_node] = True
                q.append((next_node, total_weight))

    max_value = max(distance)  # 가장 큰 노드의 값
    max_node = 0 # 가장 큰 노드

    for i in range(1, v + 1):
        # 가장 큰 노드 값 찾기
        if distance[i] == max_value:
            max_node = i
            break
    
    # 2번쨰 BFS 가장 큰 노드에서 시작해서 긴 값을 찾는다.
    q = deque([(max_node, 0)])
    visited = [False] * (v + 1)  # 방문 처리
    visited[max_node] = True
    distance = [0] * (v + 1)  # 비용

    while q:
        node, weight = q.popleft()

        for next_node, next_wegiht in graph[node]:
            total_weight = weight + next_wegiht   # 가중치 총합
            
            if not visited[next_node]:
                distance[next_node] = max(total_weight, distance[next_node])  # 새로운 가중치 값이 더 크면 새롭게 갱신
                visited[next_node] = True
                q.append((next_node, total_weight))

    answer = max(distance)  # 가장 큰 노드의 값
        
    return answer


# 문제의 입력을 받은 main() function
def main():
    import sys
    input = sys.stdin.readline

    v = int(input())  # 정점의 개수

    graph = {i: [] for i in range(1, v + 1)}  # 그래프 초기화

    for _ in range(v):
        data = list(map(int, input().split()))
        node = data[0]
        idx = 1
        while data[idx] != -1:
            neighbor = data[idx]
            distance = data[idx + 1]
            graph[node].append((neighbor, distance))
            idx += 2

    print(solution(v, graph))  # 테스트용 출력 (지우거나 수정 가능)


if __name__ == "__main__":
    main()