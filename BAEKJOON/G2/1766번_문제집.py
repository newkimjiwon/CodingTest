import heapq

# 문제 조건: 위상 정렬, 우선순위 큐(힙)
# n은 문제의 수 m은 먼저 푸는 것이 좋은 문제에 대한 정보의 개수
n, m = map(int ,input().split())

indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def toplogy_sort():
    result = []
    # 힙 배열
    heap = []

    for i in range(1, n + 1):
        if indegree[i] == 0:
            heapq.heappush(heap, i)
    
    while heap:
        current = heapq.heappop(heap)
        result.append(current)
        for i in graph[current]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(heap, i)
    
    for i in result:
        print(i, end = ' ')

toplogy_sort()