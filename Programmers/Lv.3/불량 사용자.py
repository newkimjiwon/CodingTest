from collections import defaultdict


def is_match(user, banned):
    if len(user) != len(banned):
        return False
    for u, b in zip(user, banned):
        if b != '*' and u != b:
            return False
    return True


def solution(user_id, banned_id):

    # 각 banned_id[i]에 매칭 가능한 user_id 인덱스 리스트
    candidates = defaultdict(list)

    for i in range(len(banned_id)):
        for j in range(len(user_id)):
            if is_match(user_id[j], banned_id[i]):
                candidates[i].append(j)

    results = set()

    def dfs(depth, used, path):
        if depth == len(banned_id):
            # 중복 유저 없는 경우만 저장
            key = tuple(sorted(path))
            results.add(key)
            return

        for uid in candidates[depth]:
            if uid not in used:
                dfs(depth + 1, used | {uid}, path + [uid])

    dfs(0, set(), [])

    return len(results)