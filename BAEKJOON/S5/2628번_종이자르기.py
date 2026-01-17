from collections import deque


def solution(width, length, N, cutting):
    # paper 큐에는 (x좌표 시작, y좌표 시작, 가로길이, 세로길이)를 저장합니다.
    paper = deque([(0, 0, width, length)])

    for status, cut in cutting:
        # 현재 큐에 있는 모든 조각을 꺼내서 이번 절단선에 걸리는지 확인합니다.
        for _ in range(len(paper)):
            x, y, w, l = paper.popleft()

            if status == 0:  # 가로로 자르기 (y축 기준 절단)
                # 절단선 cut이 현재 조각의 y범위(y ~ y+l) 사이에 있는지 확인
                if y < cut < y + l:
                    paper.append((x, y, w, cut - y))          # 위쪽 조각
                    paper.append((x, cut, w, l - (cut - y)))  # 아래쪽 조각
                else:
                    paper.append((x, y, w, l))                # 범위 밖이면 그대로 다시 넣기
            
            else:  # 세로로 자르기 (x축 기준 절단)
                # 절단선 cut이 현재 조각의 x범위(x ~ x+w) 사이에 있는지 확인
                if x < cut < x + w:
                    paper.append((x, y, cut - x, l))          # 왼쪽 조각
                    paper.append((cut, y, w - (cut - x), l))  # 오른쪽 조각
                else:
                    paper.append((x, y, w, l))

    # 모든 조각의 넓이 중 최댓값을 찾습니다.
    max_area = 0
    for x, y, w, l in paper:
        max_area = max(max_area, w * l)
    
    return max_area


if __name__=="__main__":
    width, length = map(int, input().split())  # 가로, 세로의 길이
    N = int(input())  # 점선의 개수
    cutting = []

    for _ in range(N):
        row, point = map(int, input().split())  # (어떻게 자를 지, 점선 번호)
        cutting.append((row, point))  # 어떻게 자를지

    print(solution(width, length, N, cutting))