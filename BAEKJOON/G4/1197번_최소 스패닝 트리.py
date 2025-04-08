import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


# 유니온 파인드용 함수
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  # 경로 압축
    return parent[x]


def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)
    if root_a != root_b:
        parent[root_b] = root_a  # 한 쪽으로 합침


def main():
    V, E = map(int, input().split())
    edges = []

    for _ in range(E):
        a, b, cost = map(int, input().split())
        edges.append((cost, a, b))

    # 가중치 기준으로 정렬
    edges.sort()

    # 각 노드의 부모를 자기 자신으로 초기화
    parent = [i for i in range(V + 1)]

    mst_weight = 0
    for cost, a, b in edges:
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            mst_weight += cost

    print(mst_weight)


if __name__ == "__main__":
    main()