def dfs(path, depth):
    if depth == M:
        print(' '.join(map(str, path)))
        return

    for i in range(len(N_list)):
        dfs(path + [N_list[i]], depth + 1)

# 입력 처리
N, M = map(int, input().split())
raw_list = list(map(int, input().split()))

# 중복 제거 + 정렬
N_list = sorted(set(raw_list))

# DFS 실행
dfs([], 0)