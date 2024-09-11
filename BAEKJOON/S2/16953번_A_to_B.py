from collections import deque

def bfs(start, end):
    # 큐 생성 (값과 현재까지의 연산 수를 저장)
    queue = deque([(start, 1)])  # (현재 값, 단계 수)
    
    while queue:
        current, cnt = queue.popleft()
        
        # 도착 조건
        if current == end:
            return cnt
        
        # 두 가지 연산 수행
        num1 = current * 2
        num2 = current * 10 + 1
        
        # end보다 작을 때만 다음 단계로 이동
        if num1 <= end:
            queue.append((num1, cnt + 1))
        if num2 <= end:
            queue.append((num2, cnt + 1))
    
    return -1

A, B = map(int, input().split())

print(bfs(A, B))
