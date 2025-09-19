import heapq

def solution(n, k, enemy):
    # 무적권으로 전부 막을 수 있으면 바로 종료
    if k >= len(enemy):
        return len(enemy)

    max_heap = []   # 지금까지 나온 적 수를 음수로 push (사실상 max-heap)
    soldiers = n

    for i, e in enumerate(enemy):
        soldiers -= e
        heapq.heappush(max_heap, -e)  # 이번 라운드 포함해 후보에 올려둔다

        # 병사가 모자라면, 지금까지 중 가장 큰 라운드를 무적권으로 되돌린다
        if soldiers < 0:
            if k == 0:
                return i  # 더 못 막음: i 라운드 직전까지 막았다
            k -= 1
            largest = -heapq.heappop(max_heap)  # 가장 큰 라운드 하나 무적 처리
            soldiers += largest                 # 그만큼 병사 소모를 되돌림

    # 끝까지 막음
    return len(enemy)