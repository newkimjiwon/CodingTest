import heapq

# 최소 힙 예시
min_heap = []

# 힙에 값 추가
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 3)

# 힙의 상태 출력
print("Min Heap:", min_heap)  # [1, 5, 3]

# 최솟값을 꺼내기
min_val = heapq.heappop(min_heap)
print("Popped Min Value:", min_val)  # 1
print("Min Heap after pop:", min_heap)  # [3, 5]

# 최대 힙 예시
max_heap = []

# 힙에 값 추가 (부호를 반대로 해서 추가)
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -3)

# 힙의 상태 출력 (부호를 다시 돌려서 출력)
print("Max Heap:", [-x for x in max_heap])  # [5, 1, 3]

# 최댓값을 꺼내기 (부호를 다시 돌려서 꺼내기)
max_val = -heapq.heappop(max_heap)
print("Popped Max Value:", max_val)  # 5
print("Max Heap after pop:", [-x for x in max_heap])  # [3, 1]