from collections import deque

def solution(n, k, peoples):
    # 정답 배열
    answer = '<'

    # 자료구조 q를 이용한 풀이
    q = deque(peoples)

    # 순번을 계산할 카운트
    count = 0

    while q:
        count += 1
        if count == k:
            answer += str(q.popleft())
            answer += ', '
            count = 0
        else:
            front = q.popleft()
            q.append(front)
    
    # 괄호
    answer = answer[:-2] + '>'

    return answer
    
if __name__ == "__main__":
    n, k = map(int, input().split())

    circle = [i for i in range(1, n + 1)]

    print(solution(n, k, circle))