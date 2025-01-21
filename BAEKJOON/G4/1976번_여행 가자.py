
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  # 경로 압축
    return parent[x]


def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)

    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1


def main():
    # 입력
    n = int(input())  # 도시의 수
    m = int(input())  # 여행 계획에 포함된 도시의 수

    # 초기화
    parent = list(range(n + 1))
    rank = [0] * (n + 1)

    # 그래프 정보 입력 및 Union-Find로 연결
    for i in range(1, n + 1):
        edges = list(map(int, input().split()))
        for j in range(1, n + 1):
            if edges[j - 1] == 1:  # 연결된 경우
                union(parent, rank, i, j)

    # 여행 계획 입력
    plan = list(map(int, input().split()))

    # 여행 계획의 모든 도시가 같은 컴포넌트에 속하는지 확인
    root = find(parent, plan[0])
    for city in plan:
        if find(parent, city) != root:
            print("NO")
            return

    print("YES")


main()