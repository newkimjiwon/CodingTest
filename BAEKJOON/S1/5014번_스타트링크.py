from collections import deque


def solution(f, s, g, u, d):
    # 중복되는 층수를 가지 않기 위한 방지
    visited = [False] * (f + 1)

    dq = deque()

    # 시작 층수는 s층에서 시작
    dq.append((s, 0))
    visited[s] = True

    # 모든 방법을 탐색했을 떄 G층에 갈 수 없다면 "use the stairs" 출력
    while dq:
        x, y = dq.popleft()

        # G층에 도달 했을 떄
        if x == g:
            return str(y)
        
        # 위로 U층만큼 올라갈 떄
        x_up = x + u
        # 아래로 D층만큼 내려갈 떄
        x_down = x - d

        # 층이 있어야하고 방문하지 않았어야함
        if x_up < (f + 1) and not visited[x_up]:
            visited[x_up] = True
            dq.append((x_up, y + 1))
        if x_down > 0 and not visited[x_down]:
            visited[x_down] = True
            dq.append((x_down, y + 1))
    
    return 'use the stairs'


if __name__=="__main__":
    f, s, g, u, d = map(int, input().split())
    print(solution(f, s, g, u, d))
    """
    print(solution(10, 1, 10, 2, 1))
    print(solution(100, 2, 1, 1, 0))
    """