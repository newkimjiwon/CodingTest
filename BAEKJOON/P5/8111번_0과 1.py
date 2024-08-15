from collections import deque

def find_gusa_number(N):
    # 큐 초기화: ("1", 1 % N)로 시작
    queue = deque([("1", 1 % N)])
    visited = set([1 % N])
    
    while queue:
        current_number, remainder = queue.popleft()
        
        # 만약 나머지가 0이라면 그 수가 답이다.
        if remainder == 0:
            return current_number
        
        # 다음 숫자들: current_number에 0 또는 1을 붙인 것
        for digit in ["0", "1"]:
            new_number = current_number + digit
            new_remainder = (remainder * 10 + int(digit)) % N
            
            if new_remainder not in visited:
                visited.add(new_remainder)
                queue.append((new_number, new_remainder))
    
    return "BRAK"

# 입력 받기
T = int(input())
for _ in range(T):
    N = int(input())
    print(find_gusa_number(N))