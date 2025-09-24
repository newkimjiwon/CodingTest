def solution(orders, course):
    # 1) 각 주문을 알파벳 오름차순으로 표준화
    orders = [''.join(sorted(o)) for o in orders]

    # 2) 길이 k별 카운트 딕셔너리
    counts_by_len = {k: {} for k in course}

    # 3) DFS로 문자열 s에서 길이 k 조합 생성하여 카운팅
    def dfs(s, k, start, path, bucket):
        # 완성된 길이 k 조합
        if len(path) == k:
            key = ''.join(path)
            bucket[key] = bucket.get(key, 0) + 1
            return
        # 남은 문자로 k를 채울 수 없으면 중단 (가지치기)
        n = len(s)
        need = k - len(path)
        # i는 start..n-need 까지만 가능
        for i in range(start, n - need + 1):
            path.append(s[i])
            dfs(s, k, i + 1, path, bucket)
            path.pop()

    # 4) 각 주문에 대해, course의 k마다 DFS 실행
    for s in orders:
        n = len(s)
        for k in course:
            if n >= k:
                dfs(s, k, 0, [], counts_by_len[k])

    # 5) 각 k에서 최빈(≥2)만 수집
    answer = []
    for k in course:
        bucket = counts_by_len[k]
        if not bucket:
            continue
        max_freq = 0
        for v in bucket.values():
            if v > max_freq:
                max_freq = v
        if max_freq < 2:
            continue
        for key, v in bucket.items():
            if v == max_freq:
                answer.append(key)

    # 6) 사전순 정렬 후 반환
    answer.sort()
    return answer